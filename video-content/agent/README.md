# Agent Subfolder

This directory contains the core components of the Video Content Agent, built
using the Google ADK (Agent Development Kit). This agent is designed to provide
quick access to information about video content stored in Firestore, leveraging
Gemini for natural language understanding and response generation.

## Purpose

The primary purpose of this agent is to allow users (e.g. show directors) to
query a video content database for facts, summaries, transcripts, and details
about individuals involved in specific videos. It acts as an intelligent
interface to the processed video data.

# Get started

1. Create a copy of `.env.example` called `.env` and update the values.
2. Run `pip install -r requirements.txt`
3. Run `adk web`
