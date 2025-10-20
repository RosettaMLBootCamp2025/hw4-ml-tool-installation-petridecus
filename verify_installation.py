#!/usr/bin/env python3
"""
Verification script for HW4: ML Tool Installation

This script checks if the student has documented their installations
in the installation_report.txt file.
"""

import os
import sys
import json


def check_report_exists():
    """Check if installation_report.txt exists"""
    return os.path.exists("installation_report.txt")


def check_report_content():
    """Check if report has meaningful content"""
    if not check_report_exists():
        return False

    with open("installation_report.txt", "r") as f:
        content = f.read()

    # Check for student name
    has_name = "Student Name:" in content and "[Your Name]" not in content

    # Check for at least some tool documentation
    required_tools = [
        "LocalColabFold",
        "LigandMPNN",
        "RFdiffusion2",
        "ESMFold",
        "OpenFold",
        "Chai-1",
        "Boltz-2",
        "DiffDock-PP",
        "PLACER"
    ]

    tools_documented = sum(1 for tool in required_tools if tool in content)

    return has_name and tools_documented >= 3  # At least 3 tools documented


def check_has_cluster_info():
    """Check if HPC cluster is specified"""
    if not check_report_exists():
        return False

    with open("installation_report.txt", "r") as f:
        content = f.read()

    return "HPC Cluster:" in content and "[Cluster Name]" not in content


def main():
    """Main verification function"""
    results = {
        "report_exists": False,
        "report_has_content": False,
        "has_cluster_info": False,
        "student_name_filled": False
    }

    # Check if report exists
    if check_report_exists():
        results["report_exists"] = True
        print("✓ installation_report.txt found")

        # Check content
        with open("installation_report.txt", "r") as f:
            content = f.read()

        # Check for student name
        if "Student Name:" in content and "[Your Name]" not in content:
            results["student_name_filled"] = True
            print("✓ Student name filled in")
        else:
            print("✗ Student name not filled in")

        # Check for cluster info
        if "HPC Cluster:" in content and "[Cluster Name]" not in content:
            results["has_cluster_info"] = True
            print("✓ HPC Cluster information provided")
        else:
            print("✗ HPC Cluster information missing")

        # Check for tool documentation
        required_tools = [
            "LocalColabFold", "LigandMPNN", "RFdiffusion2",
            "ESMFold", "OpenFold", "Chai-1", "Boltz-2",
            "DiffDock-PP", "PLACER"
        ]

        tools_found = []
        for tool in required_tools:
            if tool in content:
                tools_found.append(tool)

        if len(tools_found) >= 3:
            results["report_has_content"] = True
            print(f"✓ At least 3 tools documented ({len(tools_found)} found)")
        else:
            print(f"✗ Not enough tools documented ({len(tools_found)} found, need at least 3)")

        print(f"\nTools documented: {', '.join(tools_found)}")
    else:
        print("✗ installation_report.txt not found")

    # Write results to JSON for autograder
    with open("verification_result.json", "w") as f:
        json.dump(results, f, indent=2)

    # Print summary
    print("\n" + "="*50)
    passed = sum(results.values())
    total = len(results)
    print(f"Verification: {passed}/{total} checks passed")

    if passed == total:
        print("\n🎉 Great job! Your installation report looks good!")
        print("Make sure you've actually tested all the tools on your HPC!")
        return 0
    else:
        print("\n⚠️  Some checks failed. Please review the report requirements.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
