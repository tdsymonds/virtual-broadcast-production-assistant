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
"""Pydantic models for the Video Content Agent."""

from typing import Optional

import pydantic


class VideoContent(pydantic.BaseModel):
  """Information about a video, retrieved from the video content database.

  Attributes:
    video_id: A unique identifier for the video.
    summary: A concise summary of the video's content.
    transcript: The full or partial transcript of the video's audio, allowing
      for detailed content analysis.
  """
  video_id: str
  summary: Optional[str] = None
  transcript: Optional[str] = None
