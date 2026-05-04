# Python Scripting in PLAXIS: Automating Geotechnical Analysis and Modelling Workflows

Companion code examples for the book **Python Scripting in PLAXIS: Automating Geotechnical Analysis and Modelling Workflows**.

Each script demonstrates end-to-end automation of a PLAXIS 2D model — from geometry creation and material assignment through meshing, staged construction, calculation, and post-processing of results.

## Examples

| # | Script | Description |
|---|--------|-------------|
| 1 | `1_StaticPLT.py` | Static Pile Load Test — axisymmetric model with Mohr-Coulomb soil, loading/unloading stages, and pile head displacement curve |
| 2 | `2_Dam_EQ.py` | Embankment Dam under Seismic Loading — plane strain model with zoned dam (body, core, foundation), earthquake accelerogram input, and crest acceleration time history |
| 3 | `3_Tunnel.py` | Tunnel Excavation and Support Design — plane strain model with Hoek-Brown rock, shotcrete lining, rock bolts, and crown/wall displacement curves |
| 4 | `4_Slopestability.py` | Slope Stability Analysis — plane strain bench-cut slope in Hoek-Brown rock using the strength reduction method with Factor of Safety curve |

## Requirements

- [PLAXIS 2D](https://www.bentley.com/software/plaxis/) with Remote Scripting Server (RSS) enabled
- Python 3.x
- `plxscripting` — PLAXIS Python scripting interface
- `matplotlib` — for plotting results

## Usage

1. Open PLAXIS 2D Input and enable the Remote Scripting Server (RSS).
2. Update the port numbers and password in the script to match your RSS configuration.
3. Run the script:
   ```
   python 1_StaticPLT.py
   ```

## Disclaimer

These scripts are provided "as is", without any warranties, expressed or implied. They are intended to support learning and demonstration of concepts and are not a substitute for engineering judgment or professional verification. Users must independently verify all results before applying them in analysis, design, or decision-making processes.
