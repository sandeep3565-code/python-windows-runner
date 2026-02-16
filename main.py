import subprocess
import sys
import os

# =====================================
# Hardcoded pg4uwcmd path (64-bit OS)
# =====================================
pg4uwcmd_path = r"C:\Program Files (x86)\Elnec_sw\Programmer\pg4uwcmd.exe"


# =====================================
# Helper function to execute command
# =====================================
def run_pg4uwcmd(command):
    try:
        print(f"\nRunning command: {' '.join(command)}\n")

        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print("----- STDOUT -----")
        print(result.stdout)

        print("----- STDERR -----")
        print(result.stderr)

        print(f"Return Code: {result.returncode}")

        return result.returncode

    except Exception as e:
        print(f"Execution failed: {e}")
        return 1


# =====================================
# Open project
# =====================================
def open_project(project_file_name):

    print(f"\nOpening project: {project_file_name}")

    cmd_project = [
        pg4uwcmd_path,
        f"/Prj:{project_file_name}",
        "/Demo"
    ]

    ret_project = run_pg4uwcmd(cmd_project)

    if ret_project != 0:
        print("\nFailed to load project. Exiting workflow.")
        sys.exit(1)

    print("Project opened successfully.")


# =====================================
# Save project with new name
# =====================================
def save_project(save_file_name):

    cmd_save = [
        pg4uwcmd_path,
        f"/Saveproject:{save_file_name}"
    ]

    ret_save = run_pg4uwcmd(cmd_save)

    if ret_save != 0:
        print("\nFailed to save project.")
        sys.exit(1)
    else:
        abs_path = os.path.abspath(save_file_name)
        print(f"\nProject saved successfully at: {abs_path}")


# =====================================
# Main
# =====================================
if __name__ == "__main__":

    if not os.path.exists(pg4uwcmd_path):
        print("pg4uwcmd.exe not found!")
        sys.exit(1)

    input_project = "Test_new.eprj"
    output_project = "Test_new_saved.eprj"

    if not os.path.exists(input_project):
        print(f"Project file not found: {input_project}")
        sys.exit(1)

    open_project(input_project)
    save_project(output_project)

    print("\nWorkflow completed successfully.")

