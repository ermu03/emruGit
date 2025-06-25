import setuptools

setuptools.setup(
    name="eg",
    versions="1.0",
    packages=setuptools.find_packages(),
    install_requires=["typer>=0.9.0"],
    entry_points={"console_scripts": ["eg = eg.cli:main"]},  # 格式：命令名=包.模块:函数
)
