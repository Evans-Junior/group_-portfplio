# Team Portfolio Website

This project is a static portfolio website created by our team as part of a CI/CD pipeline practice assignment. The website consists of a main landing page and individual pages for each team member, with automated deployment to GitHub Pages using GitHub Actions.

## Team Members

- **Evans Kumi**
- **Godfred**
- **Faith**
- **Elizabeth**

## Project Overview

This project aims to demonstrate CI/CD pipeline practices using GitHub Actions for continuous integration and delivery. Each team member developed their own portfolio page in a separate feature branch and merged it into the main branch following successful testing.

The CI/CD pipeline automatically deploys updates to GitHub Pages whenever changes are pushed to the main branch. This practice helps us ensure code quality and automate the deployment process.

## Setup and Repository Structure

1. **Repository Initialization**:
   - A `README.md` file and an `index.html` (landing page) were created initially.
   - Each team member created an individual HTML page in their feature branch.

2. **GitHub Pages Setup**:
   - In the repository settings, we configured GitHub Pages to use GitHub Actions for deployment.
   - The GitHub Actions workflow (`main.yaml`) handles deployment on every push to the main branch.

3. **Feature Branch Workflow**:
   - Each team member worked on their own feature branch (e.g., `evans-page`, `godfred-page`), allowing for isolated development.
   - After completing their page, each member created a pull request to merge into the main branch.

## CI/CD Pipeline with GitHub Actions

We set up a GitHub Actions workflow in `.github/workflows/main.yaml` to deploy the website automatically to GitHub Pages. The workflow includes:
   - **Building the site** (for dynamic projects, this step could include dependency installation and build commands).
   - **Testing** (for dynamic sites or projects with a testing suite).
   - **Deploying** to GitHub Pages once tests pass.

## Project URL

Our website is live at the following link: [Team Portfolio Website](https://groupportfolio-frfmd5gva4f7g3c4.canadacentral-01.azurewebsites.net/)

## Extra Challenge

For more advanced practice, we set up a workflow with steps for dependency installation, testing, building, and deploying. This approach prepares us for deploying dynamic applications with CI/CD pipelines.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Evans-Junior/group_portfplio

## Contribution and Best Practices

Each team member followed essential best practices, including:

- **Using Descriptive Commit Messages**: Each commit message clearly describes the purpose and changes made, making it easier to track project progress.
- **Creating Pull Requests for Code Review**: Team members worked in separate feature branches and submitted pull requests to integrate their changes into the main branch. This ensured code quality and consistency across the project.
- **Adhering to Proper Code Structure and Naming Conventions**: Organized directory structure, meaningful file names, and standardized HTML, CSS, and JavaScript code formats were maintained to improve readability and maintainability.

## Future Development

In the future, this project could expand to include more dynamic content using frameworks like React or Flask. Moving to a dynamic setup would involve creating a more complex CI/CD pipeline, including:

1. **Automated Dependency Installation**: Ensuring all necessary packages are installed in the CI/CD pipeline.
2. **Build Process**: Setting up commands to compile or prepare the application for deployment.
3. **Automated Testing**: Integrating tests to confirm functionality before deployment.
4. **Dynamic Deployment Environment**: Configuring the deployment to handle dynamic content, with potential integrations for databases and environment variables.

This approach would further reinforce best practices in software deployment and allow for a scalable, dynamic application.


This `README.md` file outlines the structure, CI/CD setup, and repository organization for your static website project. If you need any additional sections, feel free to ask!
