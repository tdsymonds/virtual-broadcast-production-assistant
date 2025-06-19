"""Agent for querying video content."""
from google.adk.agents import Agent
from google.cloud import firestore
import logging

db = firestore.Client()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def query_content_db(video_id: str) -> str:
  """Query the video content database to pull information about the video.

  The video content database contains the transcript, summary and more useful
  information for a content director to get fast facts about a video.

  Args:
    video_id: The ID of the video to query. This typically corresponds to the
              document ID in the 'videos' Firestore collection.

  Returns:
    A string containing a summary of the video content, or an error message
    if the video is not found.
  """
  # TODO: write me
  return f'Here is a mock summary about the video for {video_id}'

root_agent = Agent(
  name='video-content-agent',
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
