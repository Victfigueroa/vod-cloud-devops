# Infraestructura Cloud y DevOps para una Plataforma VOD – Evaluación Módulo 6

**Autor:** Victor Figueroa  
**Curso:** Módulo 6 - Tecnología Cloud y DevOps  
**Repositorio:** [github.com/Victfigueroa/vod-cloud-devops](https://github.com/Victfigueroa/vod-cloud-devops)

---

## Descripción del Proyecto

Este repositorio forma parte de la **Evaluación del Módulo 6: Diseño de Infraestructura Cloud y DevOps**. El proyecto propone una solución arquitectónica para una plataforma de **Video Bajo Demanda (VOD)** ficticia, similar a Netflix, capaz de brindar servicios de streaming, registro de usuarios y visualización de contenido en múltiples dispositivos de forma segura, escalable y global.

El desarrollo se enmarca en las necesidades de una empresa tecnológica chilena con proyección internacional, que busca integrar prácticas modernas de DevOps, infraestructura como código y automatización CI/CD.

El objetivo principal fue **diseñar e implementar la infraestructura base** para la plataforma, integrando pruebas automáticas, despliegue continuo, análisis de calidad y aprovisionamiento de recursos.

---

## Componente de Infraestructura Seleccionado: Pipeline CI/CD

La parte de infraestructura seleccionada para desarrollar fue el pipeline de integración y despliegue continuo (CI/CD). Esta elección se fundamenta en que el pipeline es el eje que conecta y automatiza todas las fases del desarrollo: desde la validación del código con SonarCloud, hasta el despliegue de infraestructura con Terraform y la ejecución del código en entornos reales.

El pipeline actúa como columna vertebral del proyecto, garantizando entregas frecuentes, controladas y seguras. Su implementación permite reducir errores manuales, mejorar la calidad del software y acelerar el time-to-market, pilares esenciales en cualquier iniciativa DevOps moderna.

---

## Tecnologías y Herramientas Integradas

- **Python**: Lógica del backend, incluyendo pruebas unitarias.
- **HTML (Frontend)**: Interfaz simulada de usuario para la plataforma VOD.
- **Terraform**: Implementación de *Infraestructura como Código (IaC)*, creando recursos como buckets S3.
- **GitHub Actions**: Automatización de CI/CD a través de un pipeline completo.
- **SonarCloud**: Análisis de calidad del código y verificación de estándares.
- **GitHub Pages**: Hosting del frontend de forma pública.

---

## Descripción del Pipeline CI/CD

El pipeline se ejecuta automáticamente al hacer `push` a la rama `main` y sigue los siguientes pasos:

1. **Initialize Containers**  
2. **Checkout Code**  
3. **Setup Java for SonarCloud**  
4. **Análisis de Calidad con SonarCloud**  
5. **Ejecución de Pruebas Unitarias en Python**  
6. **Despliegue Automático del Frontend en GitHub Pages**  
7. **Instalación y Configuración de Terraform**  
8. **Inicialización del Entorno Terraform (`terraform init`)**  
9. **Planificación de Cambios (`terraform plan`)**  
10. **Aplicación de Cambios en Infraestructura (`terraform apply`)**  

Este flujo garantiza una integración continua eficiente, validando cada cambio antes de aplicarlo y manteniendo una infraestructura coherente y versionada.

---

## Automatización e Integración Continua

El uso de **GitHub Actions** permite:

- Automatizar pruebas unitarias con Python.
- Asegurar la calidad del código mediante SonarCloud.
- Generar y aplicar infraestructura reproducible con Terraform.
- Publicar automáticamente la interfaz de usuario en GitHub Pages.

Esta integración refuerza el ciclo DevOps, permitiendo entregas rápidas, fiables y auditables en cada commit.

---

## 🎬 Interfaz Simulada - DevFlix

[https://victfigueroa.github.io/vod-cloud-devops/](https://victfigueroa.github.io/vod-cloud-devops/)

> Interfaz HTML estática que emula la experiencia de usuario de una plataforma VOD moderna, como parte del entorno de desarrollo de DevFlix. Su propósito principal es representar visualmente cómo podría estructurarse una plataforma de streaming y permitir el despliegue utilizando la herramienta GitHub Pages.

> ⚠️ Esta interfaz no representa el frontend real de la plataforma, ni busca ser un producto final. Fue creada exclusivamente con fines demostrativos y para llevar a cabo el proceso de despliegue continuo (CD) mediante GitHub Pages como parte de la práctica del pipeline DevOps.

---

## Reflexiones y Aprendizajes

Este proyecto permitió aplicar de forma práctica múltiples conceptos fundamentales de Cloud Computing y DevOps, tales como:

- Diseño de infraestructura reproducible con Terraform.
- Automatización y control de calidad continuo con GitHub Actions y SonarCloud.
- Despliegue automático y versionado del frontend.
- Aplicación de mejores prácticas en CI/CD para entornos reales.

✅ Además, fortaleció ampliamente la comprensión de los flujos de entrega continua, la integración de herramientas en pipelines automatizados, la infraestructura como código y las buenas prácticas de despliegue en la nube. Este proceso permitió consolidar habilidades clave en entornos modernos de desarrollo de software, desde la automatización hasta el monitoreo. Todo esto con un enfoque completamente DevOps, orientado a la nube y basado en tecnologías de consumo global.

---


© 2025 – Victor Figueroa
