import pandas as pd
import numpy as np

def generate_synthetic_co2_data():
    """Generate more realistic synthetic CO2 emissions data"""
    np.random.seed(42)

    # Countries with different development patterns
    developed = ['United States', 'Germany', 'Japan', 'United Kingdom', 'France', 'Canada']
    developing = ['China', 'India', 'Brazil', 'Russia', 'South Africa', 'Indonesia']

    # Create base parameters for each country
    country_params = {}

    # Developed countries parameters (generally declining)
    for country in developed:
        country_params[country] = {
            'base': np.random.randint(1000, 5000),
            'trend': np.random.uniform(-1.5, -0.5),  # % annual change
            'volatility': np.random.uniform(0.03, 0.08),
            'energy_share': np.random.uniform(0.4, 0.6),
            'industry_share': np.random.uniform(0.2, 0.35),
            'transport_share': np.random.uniform(0.15, 0.25)
        }

    # Developing countries parameters (generally increasing)
    for country in developing:
        country_params[country] = {
            'base': np.random.randint(500, 3000),
            'trend': np.random.uniform(0.5, 3.0),  # % annual change
            'volatility': np.random.uniform(0.05, 0.12),
            'energy_share': np.random.uniform(0.5, 0.8),
            'industry_share': np.random.uniform(0.15, 0.3),
            'transport_share': np.random.uniform(0.1, 0.2)
        }

    # Special case for China - more dramatic growth
    country_params['China'] = {
        'base': 2500,
        'trend': 2.5,
        'volatility': 0.1,
        'energy_share': 0.7,
        'industry_share': 0.25,
        'transport_share': 0.15
    }

    # Generate the data
    years = np.arange(1990, 2023)
    data = []

    for country, params in country_params.items():
        # Generate base trend with volatility
        emissions = []
        current = params['base']

        for year in years:
            # Apply trend and random fluctuation
            change = params['trend'] + np.random.normal(0, params['volatility'])
            current *= 1 + change / 100
            emissions.append(max(10, current))  # Ensure positive

            # Calculate sectors
            energy = emissions[-1] * params['energy_share'] * np.random.uniform(0.95, 1.05)
            industry = emissions[-1] * params['industry_share'] * np.random.uniform(0.95, 1.05)
            transport = emissions[-1] * params['transport_share'] * np.random.uniform(0.95, 1.05)
            other = emissions[-1] - (energy + industry + transport)

            data.append({
                'Country': country,
                'Year': year,
                'Total_CO2': round(emissions[-1], 2),
                'Energy': round(energy, 2),
                'Industry': round(industry, 2),
                'Transportation': round(transport, 2),
                'Other': round(other, 2),
                'Per_Capita': round(emissions[-1] / np.random.uniform(0.5, 5), 2),  # Random population proxy
                'GDP_per_Ton': round(np.random.uniform(1000, 5000) * (1 + year - 1990) / 33, 2)  # Improving efficiency
            })

    return pd.DataFrame(data)


# Generate and save the data
co2_df = generate_synthetic_co2_data()
co2_df.to_csv('co2_emissions.csv', index=False)

# Display summary
print("Dataset summary:")
print(f"Countries: {co2_df['Country'].nunique()}")
print(f"Years: {co2_df['Year'].min()} to {co2_df['Year'].max()}")
print(f"Total records: {len(co2_df)}")
print("\nSample data:")
print(co2_df.sample(5))