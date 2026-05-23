# AWS SageMaker Delivery Setup

This guide prepares the AI Beginner Bootcamp notebooks for live delivery from Amazon SageMaker Studio JupyterLab.

## Recommended Delivery Model

Use one controlled **instructor SageMaker Studio JupyterLab space** as the source of truth during the live sessions. Learners can follow along in their own tools, but the public demo should run from an environment that has already passed the preflight checks.

Core services:

- **Amazon SageMaker Studio JupyterLab:** hosted notebook runtime for the live class.
- **Amazon S3:** backup storage for notebooks, sample PDFs, datasets, and exported artifacts.
- **Lifecycle configuration:** installs packages and prepares the bootcamp kernel when Studio starts.
- **AWS IAM execution role:** gives SageMaker only the permissions needed for S3 and optional Bedrock demos.
- **AWS Secrets Manager or environment variables:** stores external API keys without putting secrets in notebooks.
- **CloudWatch Logs:** helps debug lifecycle configuration or startup errors.

Avoid using SageMaker Studio Lab as the instructor runtime for the main live demo because compute availability and session duration can vary.

## One-Time Instructor Setup

1. Create or open a SageMaker Studio domain.
2. Create a JupyterLab space for the instructor.
3. Choose a stable CPU instance. The current notebooks do not require GPU.
4. Upload or clone this folder into the Studio file system.
5. Attach `lifecycle-config.sh` to the instructor JupyterLab space.
6. Start the JupyterLab app and select the `Python (AI Beginner Bootcamp)` kernel.
7. Run `00_preflight_check.ipynb`.
8. Fix every failed check before the first live session.

## Suggested IAM Permissions

Start with least privilege. The instructor execution role usually needs:

- Read access to the course S3 bucket.
- Write access to a limited S3 prefix for class outputs.
- CloudWatch logging access for Studio diagnostics.
- Optional: Amazon Bedrock model invocation permissions if using Bedrock demos.
- Optional: Secrets Manager read access for named secrets that store API keys.

Do not store API keys directly in notebooks, lifecycle scripts, or slide decks.

## External Model Options

The current notebooks are mostly simulated and can run without external APIs. For Day 4, choose one live model path:

| Option | Best For | Notes |
| --- | --- | --- |
| Simulated response | Maximum reliability | Best fallback for all live sessions. |
| Gemini via `google-genai` | Matching the current Day 4 Google AI Studio lesson | Requires `GEMINI_API_KEY`. |
| Amazon Bedrock via `boto3` | AWS-native delivery | Requires Bedrock model access and IAM permissions. |
| OpenAI SDK | OpenAI-centered demos | Add the SDK and use an environment variable for the key. |

For the first public run, keep the real API call short and always include a simulated fallback cell.

## Pre-Class Checklist

Run this checklist 24 hours before the bootcamp and again 30 minutes before each class:

- Open SageMaker Studio JupyterLab successfully.
- Confirm the bootcamp kernel is available.
- Run `00_preflight_check.ipynb`.
- Restart kernel and run all cells for that day's module.
- Confirm sample files or PDFs are present if used in the demo.
- Confirm `GEMINI_API_KEY` is set if using Gemini.
- Confirm `AWS_REGION` is set if using Bedrock.
- Confirm the class S3 bucket is reachable if using S3.
- Keep a browser tab open with the simulated fallback notebook section.
- Export or screenshot any critical output needed for the lesson.

## Day-by-Day Reliability Notes

### Day 1: AI Foundations and Prompting

The notebook uses local Python simulations. It should run without network access or external credentials.

### Day 2: Grounding, Embeddings, and Memory

The current embedding examples use simple local vectors. If you introduce real embeddings, test the provider call in `00_preflight_check.ipynb` before class.

### Day 3: Agents and Tools

The tool-calling demo is simulated. If you add real API actions such as email, spreadsheets, or databases, use test accounts and dry-run outputs.

### Day 4: Technical Foundations and APIs

This is the highest-risk day because live model calls depend on credentials, network access, SDK versions, region, and provider availability. Keep a working simulated response directly below any real API cell.

### Day 5: Quality, Security, and Going Live

The guardrail demo is local and reliable. For live security examples, avoid using real customer data or secrets.

## Troubleshooting

| Symptom | Likely Cause | Fix |
| --- | --- | --- |
| Kernel missing | Lifecycle config did not finish | Run `python -m ipykernel install --user --name ai-beginner-bootcamp --display-name "Python (AI Beginner Bootcamp)"`. |
| Import errors | Dependencies not installed in selected kernel | Run `python -m pip install -r requirements.txt` from the same kernel. |
| Gemini call fails | Missing or invalid `GEMINI_API_KEY` | Set the key as an environment variable or use the simulated fallback. |
| Bedrock call fails | Region/model/IAM issue | Confirm model access, `AWS_REGION`, and execution role permissions. |
| S3 access fails | IAM permission or bucket name issue | Confirm bucket name and role policy. |
| Lifecycle config fails | Script limit, path, or permission issue | Check CloudWatch logs and run the commands manually in a terminal. |

## Instructor Rule

Before teaching, every live cell should be in one of three states:

- **Runs locally with no dependencies.**
- **Runs with dependencies verified by `00_preflight_check.ipynb`.**
- **Has a tested simulated fallback immediately available.**

## AWS References

- [SageMaker JupyterLab](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl.html)
- [Lifecycle configurations in SageMaker Studio](https://docs.aws.amazon.com/en_us/sagemaker/latest/dg/studio-lifecycle-configurations.html)
- [Lifecycle configurations with JupyterLab](https://docs.aws.amazon.com/en_us/sagemaker/latest/dg/jl-lcc.html)
- [SageMaker notebook instance lifecycle configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html)
- [SageMaker Studio Lab overview](https://docs.aws.amazon.com/en_us/sagemaker/latest/dg/studio-lab-overview.html)
