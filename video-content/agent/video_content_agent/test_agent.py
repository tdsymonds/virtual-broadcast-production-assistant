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
"""Unit tests for the video content agent's database querying tool."""

from unittest.mock import MagicMock

from .agent import query_content_db
from .models import VideoContent


def test_query_content_db_success(mocker):
  mock_video_id = 'test-video-123'
  mock_transcript = 'This is a test transcript.'
  mock_summary = 'A concise test summary.'

  mock_doc = MagicMock()
  mock_doc.exists = True
  mock_doc.to_dict.return_value = {
      'transcript': mock_transcript,
      'summary': mock_summary,
  }

  mock_db = mocker.patch('video_content_agent.agent.db')
  mock_db.collection.return_value.document.return_value.get.return_value = mock_doc

  result = query_content_db(mock_video_id)

  assert isinstance(result, VideoContent)
  assert result.video_id == mock_video_id
  assert result.summary == mock_summary
  assert result.transcript == mock_transcript

  mock_db.collection.assert_called_once_with('video-data')
  mock_db.collection.return_value.document.assert_called_once_with(mock_video_id)
  mock_db.collection.return_value.document.return_value.get.assert_called_once()
