from imports import pd, np, plt, sns

df = pd.read_csv('all_data.csv')

np.random.seed(42)

I = np.random.randint(len(df['Empresa'].unique()))
company = df['Empresa'].unique()[I]
df_company = df[df['Empresa'] == company]

df_numeric = df.drop(['Año', 'Empresa'], axis = 1)


# Heatmap
cols_to_drop = [
    # Sales / operational revenue
    "Ingresos de explotación",

    # Redundant profitability metrics
    "EBIT",
    "Resultado Explotación",
    "Resultado Actividades Ordinarias",

    # Balance sheet totals
    "Total pasivo y capital propio",

    # Equity and related items
    "Otros fondos propios",
    "Valor agregado",

    # Debt / liabilities
    "Pasivo fijo",

    # Financial expense lines
    "Gastos financieros y gastos asimilados",

    # Income statement subtotals
    "Resultado bruto",
    "Resultados actividades extraordinarias",

    # Other working capital items
    "Otros activos líquidos",
    "Otros pasivos líquidos",

    # Pre‐tax profit metrics
    "Result. ordinarios antes Impuestos",

    # Tax expense
    "Impuestos sobre sociedades",

    # Fixed asset items
    "Otros activos fijos",

    # Net result and financial result
    "Resultado del Ejercicio",
    "Resultado financiero",

    # Total assets (duplicate of Total liabilities + equity)
    "Total activo"
]

df_reduced = df_numeric.drop(columns = cols_to_drop)
corr = df_reduced.corr()

mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
plt.figure(figsize = (20,20))
sns.heatmap(
   corr, 
   mask = mask,
   cmap = 'coolwarm',
   center = 0,
   fmt = ".2f",
   linewidths=0.5,
   linecolor = 'gray',
   square = True,
   cbar_kws = {"shrink": .75}
)


plt.title("Correlation between variables", pad = 80)
plt.tight_layout()
plt.savefig('../Images/correlation.png')
plt.show()



