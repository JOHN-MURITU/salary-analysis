# main.py

import explore_data
import analysis
import visualization
import report_generator

def main():
    print(" Starting Data Analysis Pipeline...\n")
    explore_data.explore()
    analysis.perform_analysis()
    visualization.visualize()
    report_generator.generate_report()
    print("\n✅ All steps complete!")

if __name__ == "__main__":
    main()
