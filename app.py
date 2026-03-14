import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title("KPIS MF 📊")
tab1,tab2,tab3 = st.tabs(["REPORTE DE RECORRIDO","REPORTE DE VENTAS","REPORTE DE PRECALES"])
with tab1 :
    base = st.file_uploader("Sube el archivo 1 a 1 BANCO ", type=[".xlsx"])
    base_interna = st.file_uploader("Sube el archivo 1 a 1 INTERNA ", type=[".xlsx"])
    if base is None and base_interna is None :
        st.warning("Debas cargar tu archivo para que tengas tu reporte")
    elif base_interna is None :
        df = pd.read_excel(base)
        supervisores = df["SUPERVISOR"].unique()
        plazas = st.multiselect("Elige a los supervisores",supervisores)
        if plazas :
            datos = df[df["SUPERVISOR"].isin(plazas)]
            jerarquia = ["SUPERVISOR","NOMBRE_EJECUTIVO"]
            opciones = st.selectbox("Elige jerarquia",jerarquia) 
            tablas1 = pd.crosstab(datos[opciones], df["TIPO_CONTACTO"])
            total = (
                tablas1.get("CONTACTO CON TITULAR",0) +
                tablas1.get("CONTACTO CON TERCERO",0) +
                tablas1.get("Sin Gestionar",0) +
                tablas1.get("NO CONTACTO",0)
                )
            total_gestionado = (
                tablas1.get("CONTACTO CON TITULAR",0) +
                tablas1.get("CONTACTO CON TERCERO",0) +
                tablas1.get("NO CONTACTO",0)
                )
            tablas1["TOTAL DATA"] = total
            tablas1["%CET"] = ((tablas1["CONTACTO CON TITULAR"] / total_gestionado) * 100).fillna(0)
            tablas1["%NC"] = ((tablas1["NO CONTACTO"]/total_gestionado)*100).fillna(0)
            tablas1["%GESTIONADO"] = (((total -tablas1["Sin Gestionar"])/total)*100).fillna(0)
            def color_cet(val):
                if val < 50 :
                    return "background-color: #ff4d4d; color: white"   # rojo
                elif val < 60:
                    return "background-color: #ffc107; color: black"   # amarillo
                else:
                    return "background-color: #28a745; color: white"   # verde
            def color_nc (val1):
                if val1 >= 50 :
                    return "background-color : #ff4d4d;color:white"
                elif val1 > 40 :
                    return "background-color : #ffc107;color:black"
                else:
                    return "background-color : #28a745;color:white"
            def color_g(val2):
                if val2 < 50 :
                    return "background-color: #ff4d4d; color: white"   # rojo
                elif val2 < 60:
                    return "background-color: #ffc107; color: black"   # amarillo
                else:
                    return "background-color: #28a745; color: white"   # verde
            st.dataframe(
                    tablas1.style
                    .format({"%GESTIONADO":"{:.2F}%","%CET": "{:.2f}%","%NC": "{:.2F}%"})
                    .applymap(color_cet, subset=["%CET"])
                    .applymap(color_nc, subset =["%NC"])
                    .applymap(color_g,subset =["%GESTIONADO"])
                    .set_properties(**{'font-weight': 'bold'})
                    )
            tablatipi = datos["DESCRIPCION_CONTACTO"].value_counts().reset_index()

            tablatipi.columns = ["DESCRIPCION_CONTACTO","LEADS"]

            tablatipi["%"] = (tablatipi["LEADS"] / tablatipi["LEADS"].sum()) * 100
            st.dataframe(
                 tablatipi.style.format({"%":"{:.2F}%"})
            )

            
    elif base is None :
        df2=pd.read_excel(base_interna)
        supervisores = df2["SUPERVISOR"].unique()
        plazas = st.multiselect("Elige a los supervisores",supervisores)
        if plazas :
            datos = df2[df2["SUPERVISOR"].isin(plazas)]
            jerarquia = ["SUPERVISOR","NOMBRE_EJECUTIVO"]
            opciones = st.selectbox("Elige jerarquia",jerarquia)
            tablas2 = pd.crosstab(datos[opciones], df2["TIPO_CONTACTO"])
            total = (
                    tablas2.get("CONTACTO CON TITULAR",0) +
                    tablas2.get("CONTACTO CON TERCERO",0) +
                    tablas2.get("Sin Gestionar",0) +
                    tablas2.get("NO CONTACTO",0)
                    )
            total_gestionado = (
                    tablas2.get("CONTACTO CON TITULAR",0) +
                    tablas2.get("CONTACTO CON TERCERO",0) +
                    tablas2.get("NO CONTACTO",0)
                    )
            tablas2["TOTAL DATA"] = total
            tablas2["%CET"] = ((tablas2["CONTACTO CON TITULAR"] / total_gestionado) * 100).fillna(0)
            tablas2["%NC"] = ((tablas2["NO CONTACTO"]/total_gestionado)*100).fillna(0)
            tablas2["%GESTIONADO"] = (((total -tablas2["Sin Gestionar"])/total)*100).fillna(0)
            def color_cet(val):
                    if val < 50 :
                        return "background-color: #ff4d4d; color: white"   # rojo
                    elif val < 60:
                        return "background-color: #ffc107; color: black"   # amarillo
                    else:
                        return "background-color: #28a745; color: white"   # verde
            def color_nc (val1):
                    if val1 >= 50 :
                        return "background-color : #ff4d4d;color:white"
                    elif val1 > 40 :
                        return "background-color : #ffc107;color:black"
                    else:
                        return "background-color : #28a745;color:white"
            def color_g(val2):
                    if val2 < 50 :
                        return "background-color: #ff4d4d; color: white"   # rojo
                    elif val2 < 60:
                        return "background-color: #ffc107; color: black"   # amarillo
                    else:
                        return "background-color: #28a745; color: white"   # verde
            st.dataframe(
                        tablas2.style
                        .format({"%GESTIONADO":"{:.2F}%","%CET": "{:.2f}%","%NC": "{:.2F}%"})
                        .applymap(color_cet, subset=["%CET"])
                        .applymap(color_nc, subset =["%NC"])
                        .applymap(color_g,subset =["%GESTIONADO"])
                        )     
            tablatipi = datos["DESCRIPCION_CONTACTO"].value_counts().reset_index()

            tablatipi.columns = ["DESCRIPCION_CONTACTO","LEADS"]

            tablatipi["%"] = (tablatipi["LEADS"] / tablatipi["LEADS"].sum()) * 100
            st.dataframe(
                 tablatipi.style.format({"%":"{:.2F}%"})
            )
    else :
      df = pd.read_excel(base)
      df2=pd.read_excel(base_interna)
      df_total = pd.concat([df,df2],ignore_index=True)
      supervisores = df_total["SUPERVISOR"].unique()
      plazas = st.multiselect("Elige a los supervisores",supervisores)
      if plazas :
          datos = df_total[df_total["SUPERVISOR"].isin(plazas)]
          jerarquia = ["SUPERVISOR","NOMBRE_EJECUTIVO"]
          opciones = st.selectbox("Elige jerarquia",jerarquia)
          tablas3 = pd.crosstab(datos[opciones], df_total["TIPO_CONTACTO"])
          total = (
                    tablas3.get("CONTACTO CON TITULAR",0) +
                    tablas3.get("CONTACTO CON TERCERO",0) +
                    tablas3.get("Sin Gestionar",0) +
                    tablas3.get("NO CONTACTO",0)
                    )
          total_gestionado = (
                    tablas3.get("CONTACTO CON TITULAR",0) +
                    tablas3.get("CONTACTO CON TERCERO",0) +
                    tablas3.get("NO CONTACTO",0)
                    )
          tablas3["TOTAL DATA"] = total
          tablas3["%CET"] = ((tablas3.get("CONTACTO CON TITULAR",0) / total_gestionado) * 100).fillna(0)
          tablas3["%NC"] = ((tablas3.get("NO CONTACTO", 0) / total_gestionado) * 100).fillna(0)
          tablas3["%GESTIONADO"] = (((total -tablas3["Sin Gestionar"])/total)*100).fillna(0)
          def color_cet(val):
                    if val < 50 :
                        return "background-color: #ff4d4d; color: white"   # rojo
                    elif val < 60:
                        return "background-color: #ffc107; color: black"   # amarillo
                    else:
                        return "background-color: #28a745; color: white"   # verde
          def color_nc (val1):
                    if val1 >= 50 :
                        return "background-color : #ff4d4d;color:white"
                    elif val1 > 40 :
                        return "background-color : #ffc107;color:black"
                    else:
                        return "background-color : #28a745;color:white"
          def color_g(val2):
                    if val2 < 50 :
                        return "background-color: #ff4d4d; color: white"   # rojo
                    elif val2 < 60:
                        return "background-color: #ffc107; color: black"   # amarillo
                    else:
                        return "background-color: #28a745; color: white"   # verde
          tablas3 = tablas3.reset_index()
          st.dataframe(
                        tablas3.style
                        .format({"%GESTIONADO":"{:.2F}%","%CET": "{:.2f}%","%NC": "{:.2F}%"})
                        .applymap(color_cet, subset=["%CET"])
                        .applymap(color_nc, subset =["%NC"])
                        .applymap(color_g,subset =["%GESTIONADO"])
                        .set_properties(**{'font-weight': 'bold'})
                        )   
          tablatipi = datos["DESCRIPCION_CONTACTO"].value_counts().reset_index()

          tablatipi.columns = ["DESCRIPCION_CONTACTO","LEADS"]

          tablatipi["%"] = (tablatipi["LEADS"] / tablatipi["LEADS"].sum()) * 100
          st.dataframe(
                 tablatipi.style.format({"%":"{:.2F}%"})
            )
with tab2:
    ventas = st.file_uploader("Sube el drive de ventas",type=[".xlsx"])
    if ventas is None :
        st.warning("Debas cargar tu archivo para que tengas tu reporte")
with tab3:
    precales = st.file_uploader("Sube el archivo de precales",type=[".xlsx"])
    if precales is None :
        st.warning("Debes cargar tu archivo para que tengas tu reporte")
    else :
        df_precal  = pd.read_excel(precales)
        supervisores = df_precal["Supervisor"].unique()
        jerarquia = ["Supervisor","NOMBRE_USUARIO"]
        colu = ["DIA","COLOR RESPUESTA BANCO"]
        plaza = st.multiselect("ELIGE SUPERVISOR",supervisores)
        df_precal["FECHA"] = pd.to_datetime(df_precal["FECHA"])
        df_precal["DIA"] = df_precal["FECHA"].dt.day
        if plaza :
            datos = df_precal[
                (df_precal["Supervisor"].isin(plaza)) &
                (df_precal["COLOR RESPUESTA BANCO"].notna()) &
                (df_precal["COLOR RESPUESTA BANCO"] != "")]
            datos_duplicados = datos.duplicated().sum()
            st.warning(f"Se detecto {datos_duplicados} precales duplicados")
            st.success("Se elimino datos vacios")
            riveros = st.selectbox("Elije jerarquia",jerarquia)
            columnas = st.selectbox("Elije vista : ",colu)
            if columnas == "DIA" :
               tabla = pd.crosstab(datos[riveros],datos[columnas])
               tabla["PROMEDIO PRECAL"] = tabla.mean(axis=1)
               st.dataframe(tabla)
            else :
                tabla = pd.crosstab(datos[riveros],datos[columnas])
                total_colores = (tabla.get("Amarillo",0)+
                                 tabla.get("Marron",0)+ 
                                 tabla.get("Plomo",0) +  
                                 tabla.get("Rojo",0) +
                                 tabla.get("Rosado",0) +
                                 tabla.get("Verde",0) +
                                 tabla.get("Verde") +
                                 tabla.get("Verde_Claro",0))
                verde_total = tabla.get("Verde", 0) + tabla.get("Verde_Claro", 0)                
                tabla["%VERDE"] = (verde_total/total_colores)*100
                st.dataframe(tabla)
                