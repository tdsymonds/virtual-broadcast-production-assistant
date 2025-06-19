# Agent Subfolder

This directory contains the core components of the Video Content Agent, built
using the Google ADK (Agent Development Kit). This agent is designed to provide
quick access to information about video content stored in Firestore, leveraging
Gemini for natural language understanding and response generation.

## Purpose

The primary purpose of this agent is to allow users (e.g., content directors) to
query a video content database for facts, summaries, transcripts, and details
about individuals involved in specific videos. It acts as an intelligent
interface to the processed video data, providing structured responses to natural
language queries.


## Setup & Local Development

1. **Navigate to Agent Directory:**
    ```bash
    cd video_content_agent
    ```
2. **Create Environment File:**
    Create a `.env` file in the `video_content_agent` based on the
    `.env.example` file.

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run Locally:**
    From the `video-content/agent` directory (one level up from
    `video_content_agent`):
    ```bash
    adk web
    ```
    This will start a local web server for your agent, typically accessible at
    `http://localhost:8000`.

## Deployment

For production deployment, refer to the [Google ADK documentation](https://developers.google.com/adk/docs/deploy). Ensure that the deployment environment has the `FIRESTORE_DATABASE_NAME` environment variable configured with the correct Firestore database name. The service account running the agent must have `Cloud Datastore Viewer` permissions for the specified database.

## Running Tests

To run the unit tests for this agent, you first need to install the development
dependencies, which include pytest.

1. Install development requirements:

   ```bash
   pip install -r requirements_dev.txt
   ```

2. Run the tests: Once the dependencies are installed, you can run the test
   suite using pytest:
   ```bash
   pytest .
   ```
