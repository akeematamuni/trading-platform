python_sources(
    name="api_sources",
    dependencies=["//libs/shared:shared_sources"]
)

pex_binary(
    name="app", 
    entry_point="main.py",
    dependencies=[":api_sources"]
)
