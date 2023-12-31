{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNb/MApgJmKVzM6eKUdEVH2"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "F-KHnK2_lXGb"
      },
      "outputs": [],
      "source": [
        "%%writefile ProyectoBigData.py\n",
        "\n",
        "import streamlit as st\n",
        "import requests\n",
        "from streamlit_lottie import st_lottie\n",
        "from PIL import Image\n",
        "\n",
        "imagen_gdp = Image.open(\"/content/gdp.png\")\n",
        "imagen_co2 = Image.open(\"/content/co2.png\")\n",
        "imagen_exp = Image.open(\"/content/expe.png\")\n",
        "imagen_unem = Image.open(\"/content/unem.png\")\n",
        "imagen_undern = Image.open(\"/content/undern.png\")\n",
        "\n",
        "\n",
        "\n",
        "with st.container():\n",
        "  st.title(\"PROYECTO SEGUNDO CORTE \")\n",
        "  st.header(\"Medición del Bienestar en America\")\n",
        "  st.write(\"texto por si moscas\")\n",
        "\n",
        "with st.container():\n",
        "    st.write(\"--\")\n",
        "    st.subheader(\"Resumen e Interpretación Grafica - Estadistica\")\n",
        "\n",
        "    st.image(imagen_gdp)\n",
        "    st.image(imagen_co2)\n",
        "    st.image(imagen_exp)\n",
        "    st.image(imagen_unem)\n",
        "    st.image(imagen_undern)\n",
        "\n",
        "    st.write(\"Respecto a indicadores como el GDP per cápita o desnutrición, los niveles de Colombia son bajos en contraposición a los de países de norteamérica y estando en la media respecto a los países de sudamérica \")\n",
        "    st.write(\"Colombia es el país de la región que tiene los mayores niveles de desempleo, incluso por encima de países como Argentina, Uruguay o Chile.\")"
      ]
    }
  ]
}