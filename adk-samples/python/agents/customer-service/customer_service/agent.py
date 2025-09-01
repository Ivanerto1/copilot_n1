"""Agent module for the TELCO customer service copilot (KB-only)."""
import os
import logging
import warnings

from google.adk import Agent
from google.adk.tools import VertexAiSearchTool

from .config import Config
from .prompts import GLOBAL_INSTRUCTION, INSTRUCTION
from .shared_libraries.callbacks import (
    rate_limit_callback,
    before_agent,
    before_tool,
    after_tool,
)

warnings.filterwarnings("ignore", category=UserWarning, module=".*pydantic.*")

configs = Config()
logger = logging.getLogger(__name__)

DATASTORE_ID = os.getenv("VERTEX_SEARCH_DATASTORE_ID", "").strip()
if not DATASTORE_ID:
    raise RuntimeError(
        "Falta VERTEX_SEARCH_DATASTORE_ID. Exporta la variable con el resource name de tu Data Store.\n"
        "Ej: export VERTEX_SEARCH_DATASTORE_ID='projects/<proj>/locations/us/collections/default_collection/dataStores/<id>'"
    )

# ÚNICA herramienta: KB vía Vertex AI Search
tools_list = [VertexAiSearchTool(data_store_id=DATASTORE_ID)]

root_agent = Agent(
    model=configs.agent_settings.model,          # ej: "gemini-2.5-flash" o "gemini-1.5-flash"
    global_instruction=GLOBAL_INSTRUCTION,
    instruction=INSTRUCTION,                    # asegúrate que el prompt sea telco y pida CITAS
    name=configs.agent_settings.name,
    tools=tools_list,
    before_tool_callback=before_tool,
    after_tool_callback=after_tool,
    before_agent_callback=before_agent,
    before_model_callback=rate_limit_callback,
)
