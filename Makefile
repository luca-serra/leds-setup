.PHONY: app
app:
	@streamlit run front/app.py

.PHONY: server
server:
	@uvicorn server.main:app --reload --host 0.0.0.0