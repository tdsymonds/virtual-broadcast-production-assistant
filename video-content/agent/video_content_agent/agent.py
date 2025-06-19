# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Agent for querying video content."""

import logging
import os

from google.adk.agents import Agent
from google.cloud import firestore

from .models import VideoContent


FIRESTORE_DATABASE_NAME = os.environ.get('FIRESTORE_DATABASE_NAME', '(default)')

db = firestore.Client(database=FIRESTORE_DATABASE_NAME)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def query_content_db(video_id: str) -> VideoContent:
  """Query the video content database to pull information about the video.

  The video content database contains the transcript, summary and more useful
  information for a show director to get fast facts about a video.

  Args:
    video_id: The ID of the video to query. This typically corresponds to the
              document ID in the 'videos' Firestore collection.

  Returns:
    An instance of VideoContent containing the video details.
  """
  doc_ref = db.collection('video-data').document(video_id)
  doc = doc_ref.get()
  response = VideoContent(video_id=video_id)
  if doc.exists:
    logger.info('Successfully retrieved data for video ID: %s', video_id)
    video_data = doc.to_dict()
    response.transcript = video_data.get(
        'transcript', 'No transcript available.'
    )
    response.summary = video_data.get('summary', 'No summary available.')
  else:
    logger.warning('No document found for video ID: %s', video_id)
  return response


root_agent = Agent(
    name='video_content_agent',
    model='gemini-2.5-pro',
    description=(
        'Agent to answer questions about video content from a database.'
    ),
    instruction=(
        'You are a helpful agent who can query a video content database. '
        'When asked about a video, use the `query_content_db` tool with the '
        'provided video ID to retrieve its details. Focus on providing '
        'summaries, transcripts, and information about people involved.'
    ),
    tools=[query_content_db],
)
