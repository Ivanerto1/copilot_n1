#!/bin/bash
# Activa entorno virtual
source .venv/bin/activate

# Variables de entorno del proyecto
export GOOGLE_CLOUD_PROJECT=copilot-nivel1
export GOOGLE_CLOUD_LOCATION=us
export GOOGLE_GENAI_USE_VERTEXAI=TRUE

# Data Store (ajusta si cambias de ID en el futuro)
export VERTEX_SEARCH_DATASTORE_ID="projects/copilot-nivel1/locations/us/collections/default_collection/dataStores/telcokb_1756506323883"

# Levanta la interfaz web
adk web
