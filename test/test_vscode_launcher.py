# Generated by CodiumAI
from pathlib import Path
from rockervsc.rockervsc import folder_to_vscode_container


class TestFolderToVscodeContainer:

    # Converts container name to hexadecimal string correctly
    def test_converts_container_name_to_hexadecimal(self):

        container_name = "test_container"
        path = Path("/some/path")

        container_hex, rocker_args = folder_to_vscode_container(container_name, path)

        expected_hex = "746573745f636f6e7461696e6572"
        assert container_hex == expected_hex
        assert (
            rocker_args
            == '--image-name test_container --name test_container --volume /some/path:/workspaces/test_container:Z --oyr-run-arg " --detach"'
        )

    # Handles empty container name string
    def test_handles_empty_container_name_string(self):

        container_name = ""
        path = Path("/some/path")

        container_hex, rocker_args = folder_to_vscode_container(container_name, path)

        expected_hex = ""
        expected_rocker_args = (
            '--image-name  --name  --volume /some/path:/workspaces/:Z --oyr-run-arg " --detach"'
        )

        assert container_hex == expected_hex
        assert rocker_args == expected_rocker_args
