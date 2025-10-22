[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/TaxBMxpu)
# Homework 4: ML Tool Installation

**⚠️ WARNING: This is one of the hardest and most challenging assignments in this bootcamp.**

Installing machine learning tools from different developers on an HPC cluster is notoriously difficult. You will likely encounter dependency conflicts, version mismatches, CUDA compatibility issues, and other installation challenges. This is a realistic experience that every computational biologist faces when working with cutting-edge ML tools.

**IMPORTANT**: This assignment should be completed on your home HPC cluster, not on your local machine.

## Overview

In this assignment, you will install a suite of state-of-the-art machine learning tools for protein structure prediction, design, and analysis. These tools represent the current frontier of computational protein science.

## Install these tools

You must successfully install the following tools:

| Tool | Purpose | Instructions |
|------|---------|--------------|
| **LocalColabFold** | Fast AlphaFold2-based structure prediction | [Instructions](docs/localcolabfold.md) |
| **LigandMPNN** | Context-aware protein sequence design | [Instructions](docs/ligandmpnn.md) |
| **RFdiffusion2** | Atom-level protein design and active site scaffolding | [Instructions](docs/rfdiffusion2.md) |
| **ESMFold** | Fast single-sequence structure prediction | [Instructions](docs/esmfold.md) |
| **OpenFold** | Open-source AlphaFold2 implementation | [Instructions](docs/openfold.md) |
| **Chai-1** | Multi-modal biomolecular structure prediction | [Instructions](docs/chailab.md) |
| **Boltz-2** | Structure and binding affinity prediction | [Instructions](docs/boltz2.md) |
| **DiffDock-PP** | Protein-protein docking | [Instructions](docs/diffdock_pp.md) |
| **PLACER** | Protein-ligand docking and ensemble generation | [Instructions](docs/placer.md) |
| **BindCraft** | End-to-end binder design pipeline | [Instructions](docs/bindcraft.md) |

## Optional Tools

These tools are optional but recommended for those interested:

| Tool | Purpose | Instructions |
|------|---------|--------------|
| **RFdiffusion All Atom** | Predecessor to RFdiffusion2 | [Instructions](docs/rfdiffusion_all_atom.md) |
| **ESM3** | Generative protein model | [Instructions](docs/esm3.md) |

## Getting Started

1. **Choose a tool** from the table above
2. **Read the instructions** carefully for that tool (click the Instructions link)
3. **Follow the installation instructions** provided
4. **Test the installation** using the test commands provided
5. **Document your success** (see Submission section below)
6. **Repeat** for each tool

## Important HPC Considerations

### Docker vs. Singularity/Apptainer

Many of these tools provide Docker containers in their official documentation. **However, most academic HPCs do NOT support Docker for security reasons.** Instead, they support Singularity or Apptainer (which are functionally equivalent).

**Key differences**:
- Docker: `docker run --gpus all image:tag command`
- Singularity/Apptainer: `apptainer exec --nv image.sif command`

When you see Docker commands in official documentation, you'll need to use the Singularity/Apptainer equivalent. Our documentation provides HPC-friendly instructions.

### GPU Access

Most of these tools require or strongly benefit from GPU access. Make sure to:
1. Understand your cluster's GPU allocation system (SLURM, PBS, etc.)
2. Request GPUs in your job scripts
3. Load appropriate CUDA modules
4. Verify GPU access with `nvidia-smi`

### Environment Management

- Use **conda** or **mamba** (faster) for environment management
- Create separate environments for each tool to avoid conflicts
- Document which environment activates which tool

### Common Installation Challenges

You will likely encounter:
- **CUDA version mismatches**: Different tools require different CUDA versions
- **Dependency conflicts**: Tool A requires numpy<2.0 while Tool B requires numpy>=2.0
- **Compilation failures**: Missing compilers, incompatible gcc versions
- **Out of disk space**: Model weights can be 10+ GB per tool
- **Network timeouts**: Downloading large files on HPC networks can be slow

**This is normal!** Part of the learning experience is troubleshooting these issues.

## Getting Help

### Before Asking for Help

1. **Read error messages carefully** - they often contain the solution
2. **Check the official documentation** for the tool
3. **Search for the error message** online (GitHub issues, Stack Overflow)
4. **Verify your CUDA/GCC versions** match requirements
5. **Check disk space** and quotas

### When You Need Help

Contact Ian Anderson at **icanderson@ucdavis.edu** with:
- Which tool you're installing
- The complete error message
- What you've already tried
- Your HPC system name (if applicable)

## Submission

Create a file called `installation_report.txt` documenting your installations:

```
# HW4 Installation Report
Student Name: [Your Name]
HPC Cluster: [Cluster Name]

## Successfully Installed Tools

### LocalColabFold
- Installation date: [date]
- Environment name: [env name]
- Test command used: [command]
- Test result: [success/notes]

### LigandMPNN
- Installation date: [date]
- Environment name: [env name]
- Test command used: [command]
- Test result: [success/notes]

[Continue for each tool...]

## Installation Challenges

### [Tool Name]
- Challenge: [describe problem]
- Solution: [how you solved it]

[Document major challenges you overcame...]

## Optional Tools Installed

[List any optional tools you successfully installed]
```

Submit this file along with any test output files generated.

## Learning Objectives

By completing this assignment, you will:

1. Gain hands-on experience with HPC job submission and resource management
2. Understand the challenges of installing research software in HPC environments
3. Learn to troubleshoot dependency conflicts and environment management
4. Become familiar with the current landscape of ML tools for protein science
5. Develop problem-solving skills essential for computational research

## Tips for Success

1. **Install one tool at a time** - don't try to install everything at once
2. **Document everything** - keep notes on what worked and what didn't
3. **Use separate environments** - avoid dependency hell
4. **Read the docs folder README files carefully** - they contain HPC-specific guidance
5. **Be patient** - downloads and installations can take hours
6. **Ask for help early** - don't spend days stuck on one issue

## About Autograding

This assignment uses autograding to verify successful installations. The autograding simply checks if you were able to run basic test commands for each tool. **Points are meaningless** - they're just a way to give you feedback on your progress. This bootcamp is about learning, not grades.

Remember: Every installation challenge you overcome is teaching you valuable skills for your research career!

Good luck! 🚀
