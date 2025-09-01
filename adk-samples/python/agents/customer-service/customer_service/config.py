# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Configuration module for the customer service agent."""

import os
import logging
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, Field


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AgentModel(BaseModel):
    """Agent model settings."""

    name: str = Field(default="customer_service_agent")
    model: str = Field(default="gemini-2.5-flash")
    temperature: float = Field(default=0.2)          # baja creatividad → menos tokens
    max_output_tokens: int = Field(default=512)      # no dejes que se vaya a 2k+
    candidate_count: int = Field(default=1)          # solo 1 candidata, no varias


class Config(BaseSettings):
    """Configuration settings for the customer service agent."""

    model_config = SettingsConfigDict(
        env_file=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../.env"
        ),
        env_prefix="GOOGLE_",
        case_sensitive=True,
    )
    agent_settings: AgentModel = Field(default=AgentModel())
    app_name: str = "customer_service_app"
    CLOUD_PROJECT: str = Field(default="my_project")
    CLOUD_LOCATION: str = Field(default="us-central1")
    GENAI_USE_VERTEXAI: str = Field(default="1")
    API_KEY: str | None = Field(default="")
