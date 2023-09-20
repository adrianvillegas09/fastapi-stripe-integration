#################################################################################
# COMMANDS                                                                      #
#################################################################################
format:
	set -e
	isort --recursive  --force-single-line-imports app
	autoflake --recursive --remove-all-unused-imports --remove-unused-variables --in-place app
	black app
	isort app

run_dev_server:
	uvicorn app.main:app --reload

run_server:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

build_image:
	docker build --pull --rm -f "Dockerfile" -t pythonstripeintegration:latest "."

run_docker:
	docker run --rm -d  -p 8000:8000/tcp pythonstripeintegration:latest
