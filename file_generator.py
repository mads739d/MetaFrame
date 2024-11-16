import json
import os

def load_json(file_path):
    """Load a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{file_path}'. {e}")
        exit(1)

def create_project_structure(base_path, config, templates):
    """Create the folder structure and populate it with initial files."""
    project_name = config['project_name']
    project_path = os.path.join(base_path, project_name)
    os.makedirs(project_path, exist_ok=True)

    # Backend
    backend = config.get('backend', {})
    backend_framework = backend.get('framework')
    if backend_framework in templates['backend']:
        backend_path = os.path.join(project_path, "backend")
        os.makedirs(backend_path, exist_ok=True)
        backend_template = templates['backend'][backend_framework]
        with open(os.path.join(backend_path, "app.py"), 'w') as f:
            f.write(backend_template.format(project_name=project_name))
    else:
        print(f"Warning: Unsupported backend framework '{backend_framework}'")

    # Frontend
    frontend = config.get('frontend', {})
    frontend_framework = frontend.get('framework')
    if frontend_framework in templates['frontend']:
        frontend_path = os.path.join(project_path, "frontend")
        os.makedirs(frontend_path, exist_ok=True)
        frontend_template = templates['frontend'][frontend_framework]
        with open(os.path.join(frontend_path, "index.js"), 'w') as f:
            f.write(frontend_template.format(project_name=project_name))
    else:
        print(f"Warning: Unsupported frontend framework '{frontend_framework}'")

    # Database
    database = config.get('database', {})
    db_type = database.get('type')
    schema = database.get('schema') or templates['database'].get(db_type)
    if schema:
        db_path = os.path.join(project_path, "database")
        os.makedirs(db_path, exist_ok=True)
        with open(os.path.join(db_path, "schema.sql"), 'w') as f:
            f.write(schema)
    else:
        print(f"Warning: Unsupported database type '{db_type}' or no schema provided")

    print(f"Project '{project_name}' created at {project_path}")
    # Create dependencies installation script
    create_dependencies_script(project_path, config)

def create_dependencies_script(project_path, config):
    """Generate a shell script to install dependencies."""
    install_script_path = os.path.join(project_path, "install_dependencies.sh")
    with open(install_script_path, 'w') as f:
        f.write("#!/bin/bash\n\n")
        f.write("echo 'Installing dependencies...'\n\n")

        # Backend dependencies
        backend_deps = config.get('backend', {}).get('dependencies', [])
        if backend_deps:
            f.write("# Install backend dependencies\n")
            f.write("pip install " + " ".join(backend_deps) + "\n\n")

        # Frontend dependencies
        frontend_deps = config.get('frontend', {}).get('dependencies', [])
        if frontend_deps:
            frontend_path = os.path.join(project_path, "frontend")
            f.write(f"# Install frontend dependencies\n")
            f.write(f"cd {frontend_path} && npm install " + " ".join(frontend_deps) + " && cd ..\n\n")

    # Make the script executable
    os.chmod(install_script_path, 0o755)
    print(f"Dependency installation script created at {install_script_path}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate a project structure based on a JSON configuration.")
    parser.add_argument('config_path', help="Path to the project configuration JSON file")
    parser.add_argument('templates_path', help="Path to the templates JSON file")
    parser.add_argument('--output', default='./', help="Output directory for the project (default: current directory)")

    args = parser.parse_args()

    config = load_json(args.config_path)
    templates = load_json(args.templates_path)

    create_project_structure(args.output, config, templates)

if __name__ == "__main__":
    main()
