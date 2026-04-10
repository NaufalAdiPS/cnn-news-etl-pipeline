# cnn-news-etl-pipeline
ETL pipeline for extracting CNN Indonesia news data from API, transforming it with Pandas, and loading it into PostgreSQL staging tables.



# CNN News ETL Pipeline

An end-to-end ETL pipeline built with Python, Pandas, and PostgreSQL to extract news data from a public API, transform it into a clean and structured format, and load it into a staging table for further analysis.

## Overview

This project was developed as part of an ETL assignment to demonstrate the complete workflow of:

- **Extract** data from an external API
- **Transform** and clean the data using Pandas
- **Load** the processed data into PostgreSQL
- **Log** the ETL process for monitoring and debugging

The dataset is sourced from the following API:

`https://berita-indo-api.vercel.app/v1/cnn-news`

## Objectives

- Retrieve CNN news data from an external API
- Select and rename relevant columns
- Remove duplicate records
- Handle missing values
- Normalize text fields
- Add derived columns for analysis
- Load the final data into a PostgreSQL staging table
- Record ETL activity using Python logging

## Tech Stack

- **Python**
- **Pandas**
- **Requests**
- **PostgreSQL**
- **psycopg2**
- **Logging**

## ETL Workflow

### 1. Extract
The pipeline fetches news data from the API and stores it in a Pandas DataFrame.

Extracted fields include:
- `title`
- `link`
- `contentSnippet`
- `isoDate`

### 2. Transform
The data is cleaned and transformed with the following steps:

- Select relevant columns
- Rename columns:
  - `title` → `news_title`
  - `link` → `news_link`
  - `contentSnippet` → `news_summary`
  - `isoDate` → `published_at`
- Remove duplicate rows based on `news_link`
- Handle missing values in `news_title` and `news_summary`
- Normalize text:
  - `news_title` to Title Case
  - `news_summary` to lowercase
- Add derived columns:
  - `title_length`
  - `word_count`
- Filter records with `word_count > 5`

### 3. Load
The transformed data is loaded into a PostgreSQL staging table named:

`stg_news`

The pipeline uses a **truncate-insert** approach to avoid duplicate data and ensure only the latest processed records are stored.

### 4. Logging
All ETL activities are logged into:

`etl_log.txt`

The logs include:
- ETL start time
- ETL finish time
- Number of extracted records
- Number of transformed records
- Number of loaded records
- Error messages if any stage fails

## Database Schema

The `stg_news` table contains the following columns:

- `news_title`
- `news_link`
- `news_summary`
- `published_at`
- `title_length`
- `word_count`

## Project Structure

```bash
cnn-news-etl-pipeline/
│
├── main.py
├── extract.py
├── transform.py
├── load.py
├── db_config.py
├── etl_log.txt
├── requirements.txt
└── README.md
