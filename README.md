# cosmic-ray-cloud-analysis
Analysis of cosmic ray and cloud cover correlation using RAG system

# Cosmic Ray - Cloud Cover Correlation Analysis

A RAG (Retrieval-Augmented Generation) system for analyzing scientific literature 
on the correlation between cosmic ray intensity and cloud cover.

## Background

This project is based on the 2009 paper:

**"On the correlation between cosmic ray intensity and cloud cover"**  
Erlykin A.D., Gyalai G., Kudela K., Sloan T., Wolfendale A.W.  
*Journal of Atmospheric and Solar-Terrestrial Physics*, 2009

The system retrieves related scientific papers and uses Claude AI to analyze 
how the scientific consensus has evolved since 2009.


## How It Works

```
NASA ADS Database → CSV export → Claude AI Analysis → Research Summary
```
## Requirements

- Python 3.x
- Anthropic API key (https://console.anthropic.com)

## Installation

```bash
pip install requests pandas python-dotenv
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/gyalai-gyula/cosmic-ray-cloud-analysis.git
```

2. Create `.env` file with your API key:
ANTHROPIC_API_KEY=your-key-here

3. Run the analysis:

```bash
python cosmic_ray_rag.py
```

## Files

| File | Description |
|------|-------------|
| `cosmic_ray_rag.py` | Main RAG system |
| `nasa_ads.csv` | Scientific papers database |
| `rag_analysis.txt` | Latest analysis results |

## Results

The system analyzes whether the 2009 findings have been confirmed or refuted 
by subsequent research, particularly the CERN CLOUD experiments (2010-2017).

## Author

Gyalai Gyula  
Electrical Engineer

