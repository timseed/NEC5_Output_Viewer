import re
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path


def extract_radiation_patterns(file_path):
    radiation_data = []

    with open(file_path, "r") as file:
        lines = file.readlines()

        # Skip the header lines by finding the start of the data section
        data_start = False
        for line in lines:
            if "- - - RADIATION PATTERNS - - -" in line:
                data_start = True
            elif data_start:
                # Regular expression to capture the radiation pattern data
                # We expect columns for THETA, PHI, VERT DB, HOR DB, TOTAL DB, MAGNITUDE, PHASE (etc.)
                match = re.match(
                    r"([0-9\.\-]+)\s+([0-9\.\-]+)\s+([0-9\.\-]+)\s+([0-9\.\-]+)\s+([0-9\.\-]+)\s+([0-9\.\-]+)\s+([0-9\.\-]+)\s+(\S+)\s+([0-9\.\-]+[E]?[+]?[0-9\.\-]*)\s+([0-9\.\-]+)\s+([0-9\.\-]+[E]?[+]?[0-9\.\-]*)\s+([0-9\.\-]+)",
                    line.strip(),
                )

                if match:
                    # Extract the relevant data fields
                    theta = float(match.group(1))
                    phi = float(match.group(2))
                    vert_db = float(match.group(3))
                    hor_db = float(match.group(4))
                    total_db = float(match.group(5))
                    axial_ratio = float(match.group(6))
                    tilt_angle = float(match.group(7))
                    polarization = match.group(8)  # LINEAR or other types
                    #                 print(f"e_theta_mag is {match.group(9)}")
                    #                 print(f"{line}")
                    e_theta_mag = float(match.group(9))
                    e_theta_phase = float(match.group(10))
                    e_phi_mag = float(match.group(11))
                    e_phi_phase = float(match.group(12))

                    # Store the data as a tuple
                    radiation_data.append(
                        (
                            theta,
                            phi,
                            vert_db,
                            hor_db,
                            total_db,
                            axial_ratio,
                            tilt_angle,
                            tilt_angle,
                            polarization,
                            e_theta_mag,
                            e_theta_phase,
                            e_phi_mag,
                            e_phi_phase,
                        )
                    )
    #             else:
    #                 print(f"Unmatched {line}")

    return radiation_data


def plot_rad(ant_name: str, radiation_data: list):
    # Extract THETA and TOTAL DB from the data
    theta = [row[0] for row in radiation_data]  # THETA (angles)
    total_db = [row[4] for row in radiation_data]  # TOTAL DB

    # Plot the radiation pattern
    plt.plot(theta, total_db)
    plt.xlabel("Theta (degrees)")
    plt.ylabel("Total Power Gain (dB)")
    plt.title(f"{ant_name} Radiation Pattern (Total Gain vs. Theta)")
    plt.grid(True)
    plt.savefig(f"{ant_name}.png")


def plot_pattern(ant_name: str, radiation_data: list):
    theta = [row[0] for row in radiation_data]  # THETA (angles, in degrees)
    total_db = [row[4] for row in radiation_data]  # TOTAL DB (gain in dB)

    # Convert theta to radians for polar plot
    theta_rad = np.radians(theta)

    # Create the polar plot
    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, projection="polar")
    ax.plot(theta_rad, total_db, label="Total Gain (dB)", color="b")

    # Labels and Title
    ax.set_title(f"{ant_name} Radiation Pattern", va="bottom")
    ax.set_xlabel("Theta (degrees)")
    ax.set_ylabel("Total Power Gain (dB)")

    # Show the plot
    plt.savefig(f"{ant_name}_rad_pattern.png")


if __name__ == "__main__":
    nec_5_output = sys.argv[1]
    ant_name = Path(nec_5_output).stem
    # Example usage
    radiation_data = extract_radiation_patterns(nec_5_output)
    plot_rad(ant_name, radiation_data)
    plot_pattern(ant_name, radiation_data)
    print(f"Ant:{ant_name} has been processed")
