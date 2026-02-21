# Métricas para Calcular r - Coeficiente de Transferencia y Derivación

## Definición Operacional de r

En la fórmula $K(t) = K_0(1 + r)^t$, **r** es el **Coeficiente de Transferencia y Derivación**.

### Interpretación

| Valor de r | Significado | Consecuencia |
|------------|-------------|--------------|
| **r → 0** | Conocimiento rígido | Solo sirve para examen/tarea específica, no se transfiere |
| **r < 0** | Deuda técnica | Lagunas que bloquean aprendizaje futuro |
| **r > 0** | Conocimiento generativo | Modelo mental que resuelve problemas en dominios diferentes |

---

## Las 3 Métricas para Calcular r

### Jerarquía de Dependencia

```
Métrica 1 (Derivación) → Métrica 2 (Transferencia) → Métrica 3 (Velocidad)
```

**Regla crítica**: No se puede transferir lo que no se puede derivar. No se puede acelerar lo que no se puede transferir.

---

## Métrica 1: Profundidad de Derivación (Integridad Lógica)

> "¿Puedo reconstruir el edificio si me quitan los planos?"

### El Test

Tomar un concepto clave que se cree "saber" (fórmula, estrategia, código).

### La Operación

1. Tomar hoja en blanco
2. Sin mirar ninguna referencia
3. **Derivar** el concepto desde axiomas básicos
4. No escribirlo de memoria, sino demostrar lógicamente por qué es inevitable

### Cálculo de r

| Resultado | Valor de r | Acción |
|-----------|------------|--------|
| Escribir de memoria sin entender | r = 0 | Volver a fundamentos |
| Trabarse a la mitad | r < 0 | Hay lagunas, identificarlas |
| Llegar desde axioma hasta conclusión | r > 0 | Continuar |

### Ejemplos

**Concepto: Teorema de Pitágoras**
- ❌ Escribir "a² + b² = c²" de memoria
- ✅ Derivar geométricamente usando áreas de cuadrados

**Concepto: Patrón Strategy**
- ❌ Escribir el diagrama UML de memoria
- ✅ Derivar desde el problema de "if/switch on type" y el principio OCP

---

## Métrica 2: Distancia Semántica (Capacidad de Transferencia)

> "El valor de un principio fundamental es que es universal"

### El Test

Tomar el principio estudiado y aplicarlo a un sistema completamente ajeno.

### Niveles de Distancia

| Nivel | Ejemplo con "Selección Natural" | Valor de r |
|-------|----------------------------------|------------|
| **Bajo** | Aplicar a otro animal | r bajo |
| **Medio** | Aplicar a algoritmos genéticos | r medio |
| **Alto** | Aplicar a economía de mercado o psicología | r alto |

### La Operación

1. Identificar el principio fundamental (no el hecho específico)
2. Encontrar un sistema en un dominio diferente
3. Mapear el principio al nuevo sistema
4. Verificar que las predicciones se mantengan

### Cálculo de r

Medir la **distancia** entre dominio original y dominio de aplicación:
- A mayor distancia sin perder precisión lógica, mayor r
- Si pierde precisión al transferir, el principio no está bien abstraído

### Ejemplos de Transferencia Exitosa

| Principio Original | Dominio Origen | Transferencia Alta |
|--------------------|----------------|-------------------|
| Selección Natural | Biología | Competencia de startups |
| Ley de Pareto | Economía | Bugs en código (20% causa 80% de crashes) |
| Entropía | Termodinámica | Degradación de sistemas de software |
| Retroalimentación negativa | Control | Equipos auto-organizados |

---

## Métrica 3: Delta de Tiempo en Adquisición (Δt)

> "Si entiendo los fundamentos, el siguiente concepto debe ser más fácil"

### El Test

Medir el tiempo para aprender concepto nuevo (C₁) basado en el anterior (C₀).

### La Fórmula

$$r \propto \frac{1}{\Delta t}$$

### Interpretación

| Patrón Observado | Valor de r | Diagnóstico |
|------------------|------------|-------------|
| Cada tema cuesta igual | r = 0 | No hay composición, solo apilamiento |
| Cada tema cuesta más | r < 0 | Hay lagunas acumulándose |
| Cada tema cuesta menos | r > 0 | El interés está componiendo |

### Ejemplo Práctico

**Secuencia de aprendizaje en POO:**

| Concepto | Tiempo esperado (r alto) | Tiempo real (r bajo) |
|----------|--------------------------|---------------------|
| Fundamentos POO | 10 horas | 10 horas |
| Herencia/Polimorfismo | 3 horas | 8 horas |
| Patrón Strategy | 30 minutos | 5 horas |
| Patrón Factory | 15 minutos | 4 horas |

Si cada patrón toma horas en lugar de minutos, los fundamentos de POO no fueron internalizados.

---

## Sistema de Evaluación Integrado

### Reglas Operacionales

```
SI fallo Métrica 1:
    r = 0
    ACCIÓN: Volver a los axiomas, no importa el resto
    
SI paso Métrica 1 pero fallo Métrica 2:
    r = bajo
    DIAGNÓSTICO: Entiendo pero no generalizo
    ACCIÓN: Más ejemplos en dominios distintos
    
SI paso Métricas 1 y 2 pero fallo Métrica 3:
    r = medio
    DIAGNÓSTICO: Tengo conocimiento pero no automatizado
    ACCIÓN: Más práctica deliberada
    
SI paso las 3 Métricas:
    r = alto
    ACCIÓN: Avanzar al siguiente tema
```

### Checklist de Evaluación

Después de cada sesión de estudio, responder:

- [ ] ¿Puedo derivar el concepto desde cero en hoja en blanco?
- [ ] ¿Puedo dar al menos 2 ejemplos en dominios diferentes?
- [ ] ¿Este concepto fue más fácil que el anterior del mismo tema?

Si alguna respuesta es "no", identificar qué métrica falló y aplicar la acción correspondiente.

---

## Señales de Alerta

### r = 0 (Conocimiento Muerto)

- Necesitar siempre las notas para recordar
- No poder explicar "por qué" funciona algo
- Sentir que cada tema es "empezar de cero"

### r < 0 (Deuda Técnica Cognitiva)

- Confusión creciente al avanzar
- Temas nuevos contradicen lo que "sabía"
- Sensación de "no entiendo nada últimamente"

### r > 0 (Composición Saludable)

- Poder predecir conceptos antes de aprenderlos
- Ver conexiones entre dominios aparentemente distintos
- Aprender más rápido con el tiempo
