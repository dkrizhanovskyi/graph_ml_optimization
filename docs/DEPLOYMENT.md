# Deployment Guide for Graph ML Optimization Project

This guide outlines the steps required to deploy the Graph ML Optimization Project using Docker and GitHub Actions CI/CD pipeline.

## Prerequisites

Before you begin, ensure you have the following:
- A server with Docker installed.
- SSH access to the server.
- Docker Hub account (for storing Docker images).
- GitHub repository with access to GitHub Actions.

## 1. Setting Up Environment Variables

To securely deploy your application, set up the following secrets in your GitHub repository:

- `DOCKER_USERNAME`: Your Docker Hub username.
- `DOCKER_PASSWORD`: Your Docker Hub password or access token.
- `SERVER_HOST`: The IP address or hostname of your deployment server.
- `SERVER_USER`: The username used to SSH into your server.
- `SERVER_SSH_KEY`: The private SSH key (in PEM format) used to authenticate with your server.

## 2. Configuring GitHub Actions CI/CD Pipeline

The CI/CD pipeline is defined in `.github/workflows/ci.yml`. This pipeline will:
- Run tests on every push or pull request to the `main` branch.
- Build a Docker image if the tests pass.
- Push the Docker image to Docker Hub.
- Deploy the application to your server using SSH.

No additional configuration is required unless you want to customize the pipeline.

## 3. Building and Running Locally with Docker

To build and run the application locally using Docker:

```bash
docker-compose up --build
```

This command will build the Docker image and start the application on `http://localhost:5000/`.

## 4. Deploying to Production

Once your code is pushed to the `main` branch, the GitHub Actions pipeline will automatically deploy your application. Here are the steps involved:

1. **Push to `main`**: After making changes and committing them, push to the `main` branch.
2. **CI/CD Pipeline Execution**: GitHub Actions will:
   - Run tests to ensure everything is working correctly.
   - Build the Docker image.
   - Push the image to Docker Hub.
   - SSH into your server and pull the latest Docker image.
   - Restart the application with the new image.

3. **Access the Application**: Once deployed, your application will be accessible on your server's IP address or domain name.

## 5. Monitoring and Logs

To view logs from your application running in Docker:

```bash
docker logs -f graph_ml_optimization
```

If you need to restart the application manually:

```bash
docker-compose restart
```

## 6. Scaling and Extending

If you need to scale the application or add additional services (e.g., a database), you can modify the `docker-compose.yml` file accordingly. For example, to add a PostgreSQL database, uncomment the `db` service and its corresponding volume.

## 7. Troubleshooting

### Common Issues:

- **CI/CD Pipeline Failures**: Check the GitHub Actions logs for detailed error messages.
- **SSH Authentication Issues**: Ensure your SSH key is correctly configured and that the server's SSH settings allow key-based authentication.
- **Docker Issues**: Ensure Docker is running on your server and that you have sufficient permissions to run Docker commands.

For further assistance, please refer to the [GitHub Actions documentation](https://docs.github.com/en/actions) and the [Docker documentation](https://docs.docker.com/).
