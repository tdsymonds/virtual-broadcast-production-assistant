# Video Content Agent

This repository contains the implementation of a Video Content Agent designed to
intelligently process, store, and query information extracted from video files. 
The system leverages Google Cloud services for robust data handling and Google
ADK with Gemini for natural language interaction.

## Project Overview

The Video Content Agent streamlines the process of extracting valuable insights
from video assets. When a new video is uploaded to a designated Google Cloud
Storage (GCS) bucket, a Cloud Run service is triggered. This service processes
the video using Google's Generative AI (Gemini) to generate a transcript,
summary, and identify people involved. The extracted metadata is then stored in
a Google Cloud Firestore database.

The core of the system is a Google ADK agent that provides a natural language
interface to this rich video content database. Users, such as content directors,
can query the agent to quickly retrieve facts, summaries, and other relevant
information about any processed video.

## Architecture

The system follows a serverless, event-driven architecture:

1.  **Video Upload:** Videos are uploaded to a dedicated Google Cloud Storage
    (GCS) bucket.
2.  **Cloud Run Processing:** A Cloud Run service is triggered by new video
    upload events in the GCS bucket.
    * It downloads the video.
    * It uses Google's Generative AI (Gemini) to analyze the video content.
    * It extracts information such as transcripts & summaries.
    * It stores this structured data in a Google Cloud Firestore database.
3.  **Firestore Database:** Acts as the central repository for all processed
    video metadata.
4.  **ADK Video Content Agent:** An ADK-based agent that connects to the
    Firestore database.
    * Allows users to query video information using natural language.
    * Utilizes the structured data from Firestore to provide accurate and
    concise answers.

## Getting Started
Follow these steps to set up and run the Video Content Agent.

### Prerequisites
A Google Cloud Project with billing enabled.
Google Cloud SDK installed and authenticated (`gcloud auth login`,
`gcloud config set project YOUR_PROJECT_ID`). Python 3.11+ and pip installed.

1. Enable Google Cloud APIs
   Ensure the following APIs are enabled in your Google Cloud Project:

   ```bash
   gcloud services enable storage.googleapis.com run.googleapis.com firestore.googleapis.com aiplatform.googleapis.com
   ```

2. Create Cloud Storage Bucket
   Create a bucket where videos will be uploaded:

   ```bash
   gcloud storage buckets create gs://your-video-content-bucket --project=YOUR_PROJECT_ID --location=YOUR_GCS_LOCATION
   ```
    Replace your-video-content-bucket and YOUR_GCS_LOCATION.

3. Create Firestore Database
   Create a Firestore database. It's recommended to create a named database for
   this project, for example, `video-content-agent`.

    Go to the Firestore section in Google Cloud Console.
    Choose "Native mode" and select a region.
    If you choose a named database, make a note of its name (e.g.,
    video-content-agent).
