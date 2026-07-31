import arxiv
import time
import random

def search_arxiv(query, max_retries=3):
    search = arxiv.Search(
        query=query,
        max_results=3,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = []
    delay = 5  # Start with a 5-second baseline delay

    for attempt in range(max_retries):
        try:
            # 1. Enforce a mandatory delay before making the request.
            # Adding a tiny bit of random 'jitter' prevents multiple agents 
            # from hitting the API at the exact same millisecond.
            time.sleep(delay + random.uniform(0.5, 1.5))

            # 2. Try to fetch results
            results_generator = search.results()
            
            for result in results_generator:
                papers.append({
                    "title": result.title,
                    "summary": result.summary,
                    "pdf": result.pdf_url,
                    "authors": [a.name for a in result.authors]
                })
            
            # If successful, break out of the retry loop and return data
            if papers:
                return papers

        except Exception as e:
            error_message = str(e).lower()
            print("Arxiv Attempt {} failed: {}".format(attempt + 1, e))
            
            # If it's a rate limit error (HTTP 429), double the wait time and try again
            if "429" in error_message or "too many requests" in error_message:
                delay *= 2  # Exponential backoff (5s -> 10s -> 20s)
                print("Rate limited. Retrying in {} seconds...".format(delay))
                continue
            else:
                # If it's a different error, don't bother retrying
                break

    # fallback if all retries fail
    if not papers:
        papers = [{
            "title": "Arxiv temporarily unavailable",
            "summary": "Too many requests sent to Arxiv API.",
            "pdf": "",
            "authors": []
        }]
        
    return papers