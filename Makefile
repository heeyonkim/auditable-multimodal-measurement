PYTHON ?= python3

.PHONY: summary verify test check

summary:
	$(PYTHON) scripts/summarize_pilot.py --data-dir data/derived --output summary_check.json

verify:
	$(PYTHON) scripts/verify_research_object.py --check

test:
	$(PYTHON) -m unittest discover -s tests -v

check: test verify
