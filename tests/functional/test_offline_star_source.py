"""
Functional tests for sending messages in the SecureDrop client application. The
tests are based upon the client testing descriptions here:

https://github.com/freedomofpress/securedrop-client/wiki/Test-plan#basic-client-testing
"""
import pytest
from flaky import flaky
from PyQt5.QtCore import Qt

from tests.conftest import TIME_APP_START, TIME_RENDER_CONV_VIEW, TIME_RENDER_SOURCE_LIST


@flaky
@pytest.mark.vcr()
def test_offline_star_source(functional_test_logged_in_context, qtbot):
    """
    It's NOT possible to star a source when the client is offline.
    """

    gui, controller, homedir = functional_test_logged_in_context
    qtbot.wait(TIME_APP_START)

    def check_for_sources():
        assert len(list(gui.main_view.source_list.source_items.keys()))

    qtbot.waitUntil(check_for_sources, timeout=TIME_RENDER_SOURCE_LIST)
    source_ids = list(gui.main_view.source_list.source_items.keys())
    first_source_id = source_ids[0]
    first_source_item = gui.main_view.source_list.source_items[first_source_id]
    first_source_widget = gui.main_view.source_list.itemWidget(first_source_item)
    qtbot.mouseClick(first_source_widget, Qt.LeftButton)

    # Now logout.
    def check_login_button():
        assert gui.left_pane.user_profile.login_button.isVisible()

    gui.left_pane.user_profile.user_button.menu.logout.trigger()
    qtbot.waitUntil(check_login_button, timeout=TIME_RENDER_CONV_VIEW)

    # Check the source isn't checked.
    assert first_source_widget.star.isChecked() is False
    # Click it.
    qtbot.mouseClick(first_source_widget.star, Qt.LeftButton)

    def check_for_error():
        # Confirm the user interface is showing a sign-in error.
        msg = gui.top_pane.error_status_bar.status_bar.currentMessage()
        assert msg == "You must sign in to perform this action."

    qtbot.waitUntil(check_for_error, timeout=TIME_RENDER_CONV_VIEW)
