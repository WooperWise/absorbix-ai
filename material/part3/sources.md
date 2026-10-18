# Источники этапа 3 — проектирование платформы

**Дата проверки: 18 октября 2026 года.** Первичные документы используются в пределах явно указанной области. Документация изменяемого сервиса не доказывает успешную интеграцию. «Прочитано» означает просмотр указанного материала или релевантных разделов, а не аудит исходного кода, всей научной литературы либо всех нормативных требований. Дополнительные URL одного документа не являются независимыми доказательствами.

## Материалы проекта

<a id="P01"></a>
**[P01] Техническое задание DESCR(1).md.** Предоставлено пользователем. [Локальная копия](basis/DESCR.md). Источник требований, не научное доказательство.

<a id="P02"></a>
**[P02] Принятый отчёт этапа 1 в переписке и его реестр источников.** 17.10.2026. [Реестр](basis/sources_stage1.md). Сам отчёт этапа 1 находится в переписке, отдельный несуществующий файл не подменяется реконструкцией.

<a id="P03"></a>
**[P03] Полный Markdown-отчёт этапа 2.** 18.10.2026. [Отчёт](basis/report_stage2.md), [реестр](basis/sources_stage2.md). Источник предыдущих проектных выводов и рыночного сравнения; численные результаты повторно в новом отчёте не переинтерпретируются.

## Внешние первоисточники

<a id="S01"></a>
### S01. FDA. ICH Q8(R2): Pharmaceutical Development

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q8r2-pharmaceutical-development](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q8r2-pharmaceutical-development)

**Дата / версия / статус:** Final; ноябрь 2009.

**Тип:** Регуляторное руководство.

**Что просмотрено:** Официальная страница и PDF; просмотрена страница с элементами фармацевтической разработки.

**Основание для архитектуры:** Целевой профиль продукта, критические характеристики качества, связь свойств материалов и процесса с результатом.

**Предел использования:** Не предписывает выбранный программный стек и не подтверждает пригодность будущей платформы.

**Дополнительное официальное представление:** [https://www.fda.gov/media/71535/download](https://www.fda.gov/media/71535/download).

<a id="S02"></a>
### S02. FDA. ICH Q9(R1): Quality Risk Management

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q9r1-quality-risk-management](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q9r1-quality-risk-management)

**Дата / версия / статус:** Final; май 2023.

**Тип:** Регуляторное руководство.

**Что просмотрено:** Официальная страница и PDF; просмотрены положения о субъективности и неопределённости.

**Основание для архитектуры:** Управление рисками качества и необходимость учитывать неопределённость и субъективность оценок.

**Предел использования:** Проектная классификация рисков в этом отчёте не является дословной шкалой ICH.

**Дополнительное официальное представление:** [https://www.fda.gov/media/167721/download](https://www.fda.gov/media/167721/download).

<a id="S03"></a>
### S03. FDA. ICH M9: Biopharmaceutics Classification System-Based Biowaivers

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m9-biopharmaceutics-classification-system-based-biowaivers](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m9-biopharmaceutics-classification-system-based-biowaivers)

**Дата / версия / статус:** Final; май 2021.

**Тип:** Регуляторное руководство.

**Что просмотрено:** Официальная страница; предметная интерпретация согласована с первым этапом.

**Основание для архитектуры:** Область BCS-биовейвера; необходимость соответствующих данных.

**Предел использования:** В отчёте не утверждается, что один in silico прогноз устанавливает регуляторный BCS или право на биовейвер.

<a id="S04"></a>
### S04. FDA. ICH M13A: Bioequivalence for Immediate-Release Solid Oral Dosage Forms

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m13a-bioequivalence-immediate-release-solid-oral-dosage-forms](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m13a-bioequivalence-immediate-release-solid-oral-dosage-forms)

**Дата / версия / статус:** Final; октябрь 2024.

**Тип:** Регуляторное руководство.

**Что просмотрено:** Официальная страница.

**Основание для архитектуры:** Отдельный контекст задачи биоэквивалентности пероральных форм в области действия документа.

**Предел использования:** Не распространяется автоматически на все пути введения, формы и клинические ситуации.

<a id="S05"></a>
### S05. FDA. ICH M15: General Principles for Model-Informed Drug Development

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m15-general-principles-model-informed-drug-development](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m15-general-principles-model-informed-drug-development)

**Дата / версия / статус:** Final; июнь 2026.

**Тип:** Регуляторное руководство.

**Что просмотрено:** Официальная страница, текст PDF и изображения страниц с определениями и таблицей оценки.

**Основание для архитектуры:** Вопрос исследования, context of use, влияние модели, последствия неправильного решения, план оценки и документация MIDD.

**Предел использования:** Не автоматическая сертификация ПО. Поля и статусы предлагаемых контрактов — адаптация автора.

**Дополнительное официальное представление:** [https://www.fda.gov/media/184747/download](https://www.fda.gov/media/184747/download).

<a id="S06"></a>
### S06. FDA. Considerations for the Use of Artificial Intelligence to Support Regulatory Decision-Making for Drug and Biological Products

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological)

**Дата / версия / статус:** Draft; январь 2025; проверен статус 18.10.2026.

**Тип:** Проект регуляторного руководства.

**Что просмотрено:** Официальная страница, PDF, изображение страницы с этапами оценки доверия.

**Основание для архитектуры:** Риск-ориентированная оценка доверия к AI для заявленного контекста использования.

**Предел использования:** Draft / Not for implementation. Не представлять как окончательное обязательное требование к каждому исследовательскому приложению.

**Дополнительное официальное представление:** [https://www.fda.gov/media/184830/download](https://www.fda.gov/media/184830/download).

<a id="S07"></a>
### S07. EMA. Reflection paper on the use of artificial intelligence in the medicinal product lifecycle

**Ссылка:** [https://www.ema.europa.eu/en/scientific-guidelines/use-artificial-intelligence-ai-medicinal-product-lifecycle](https://www.ema.europa.eu/en/scientific-guidelines/use-artificial-intelligence-ai-medicinal-product-lifecycle)

**Дата / версия / статус:** Принят 30.09.2024.

**Тип:** Документ регулятора — reflection paper.

**Что просмотрено:** Официальная страница и PDF; просмотрены положения о данных и независимой оценке.

**Основание для архитектуры:** Разделение обучающих и тестовых данных, контроль смещений, документация и применимость результатов.

**Предел использования:** Не закон и не основание для заявления о соответствии всему регуляторному режиму.

**Дополнительное официальное представление:** [https://www.ema.europa.eu/en/documents/scientific-guideline/reflection-paper-use-artificial-intelligence-ai-medicinal-product-lifecycle_en.pdf](https://www.ema.europa.eu/en/documents/scientific-guideline/reflection-paper-use-artificial-intelligence-ai-medicinal-product-lifecycle_en.pdf).

<a id="S08"></a>
### S08. FDA. ICH Q1A(R2): Stability Testing of New Drug Substances and Products

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q1ar2-stability-testing-new-drug-substances-and-products](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q1ar2-stability-testing-new-drug-substances-and-products)

**Дата / версия / статус:** Final; 2003.

**Тип:** Регуляторное руководство.

**Что просмотрено:** Официальная страница.

**Основание для архитектуры:** Стабильность продукта — самостоятельный предмет испытаний.

**Предел использования:** Из названия эксципиента или расчётной характеристики нельзя вывести установленный срок годности.

<a id="S09"></a>
### S09. EMA. ICH Q1 guideline on stability testing of drug substances and drug products

**Ссылка:** [https://www.ema.europa.eu/en/scientific-guidelines/ich-q1-guideline-stability-testing-drug-substances-drug-products](https://www.ema.europa.eu/en/scientific-guidelines/ich-q1-guideline-stability-testing-drug-substances-drug-products)

**Дата / версия / статус:** На проверенной странице: Draft, Step 2b; опубликован 30.04.2025.

**Тип:** Проект обновлённого руководства.

**Что просмотрено:** Прочитана официальная карточка статуса.

**Основание для архитектуры:** Наличие проекта консолидированного Q1 и необходимость версионирования правил.

**Предел использования:** Закрытие консультации не означает вступление окончательной версии в силу; не объявляется действующей заменой всех прежних Q1.

<a id="S10"></a>
### S10. FDA. Part 11, Electronic Records; Electronic Signatures — Scope and Application

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application)

**Дата / версия / статус:** Guidance; сентябрь 2003.

**Тип:** Официальное разъяснение области применения.

**Что просмотрено:** Прочитано официальное описание и текст руководства на странице.

**Основание для архитектуры:** Применимость Part 11 зависит от регулируемых электронных записей и контекста использования.

**Предел использования:** Наличие журналов или кнопки согласования не делает исследовательский прототип Part 11-compliant.

<a id="S11"></a>
### S11. ISO/IEC/IEEE 42010:2022 — Architecture description

**Ссылка:** [https://www.iso.org/standard/74393.html](https://www.iso.org/standard/74393.html)

**Дата / версия / статус:** Издание 2; ноябрь 2022.

**Тип:** Международный стандарт, публичная карточка.

**Что просмотрено:** Прочитана публичная аннотация ISO, не платный полный текст.

**Основание для архитектуры:** Описание архитектуры через заинтересованные стороны, интересы и представления; стандарт не задаёт единственную архитектуру.

**Предел использования:** Полное нормативное соответствие не проверено и не заявляется.

<a id="S12"></a>
### S12. ISO/IEC 25010:2023 — Product quality model

**Ссылка:** [https://www.iso.org/standard/78176.html](https://www.iso.org/standard/78176.html)

**Дата / версия / статус:** 2023.

**Тип:** Международный стандарт, публичная карточка.

**Что просмотрено:** Прочитана публичная аннотация ISO, не платный полный текст.

**Основание для архитектуры:** Модель качества программного продукта; опубликованная редакция описывает девять характеристик.

**Предел использования:** Предложенные ниже NFR не выдаются за дословную полную таблицу стандарта.

<a id="S13"></a>
### S13. C4 model — System context and container diagrams

**Ссылка:** [https://c4model.com/diagrams/container](https://c4model.com/diagrams/container)

**Дата / версия / статус:** Действующая веб-документация; проверка 18.10.2026.

**Тип:** Документация авторов метода.

**Что просмотрено:** Прочитаны страницы context, container, component.

**Основание для архитектуры:** Разделение уровня системы, исполняемых приложений/хранилищ и внутренних компонентов.

**Предел использования:** C4 container не равен Docker-контейнеру; C4 не подтверждает научную пригодность системы.

**Дополнительное официальное представление:** [https://c4model.com/diagrams/system-context](https://c4model.com/diagrams/system-context); [https://c4model.com/diagrams/component](https://c4model.com/diagrams/component).

<a id="S14"></a>
### S14. W3C. PROV-DM: The PROV Data Model

**Ссылка:** [https://www.w3.org/TR/prov-dm/](https://www.w3.org/TR/prov-dm/)

**Дата / версия / статус:** W3C Recommendation; 30.04.2013.

**Тип:** Открытая спецификация.

**Что просмотрено:** Прочитаны определения сущностей, действий, агентов и связей происхождения.

**Основание для архитектуры:** Концептуальная модель происхождения данных.

**Предел использования:** Отчёт предлагает отображение на собственную схему; не заявляет полную PROV-совместимость и не требует графовую СУБД.

<a id="S15"></a>
### S15. The Unified Code for Units of Measure — UCUM

**Ссылка:** [https://ucum.org/ucum](https://ucum.org/ucum)

**Дата / версия / статус:** Версия 2.2; 17.06.2024.

**Тип:** Официальная спецификация единиц.

**Что просмотрено:** Прочитана официальная спецификация, разделы об обозначениях и аннотациях.

**Основание для архитектуры:** Машиночитаемые единицы и размерностная нормализация.

**Предел использования:** UCUM не заменяет сведения о химическом основании дозы, методе или типе массовой доли.

<a id="S16"></a>
### S16. JSON Schema — Draft 2020-12

**Ссылка:** [https://json-schema.org/draft/2020-12](https://json-schema.org/draft/2020-12)

**Дата / версия / статус:** Draft 2020-12; опубликованные спецификации 2022.

**Тип:** Официальная спецификация.

**Что просмотрено:** Прочитаны обзор, core/validation и назначение ключевых слов.

**Основание для архитектуры:** Контракты структуры сообщений, required, enum, композиция и валидация.

**Предел использования:** Структурная корректность JSON не доказывает научную истинность; format должен явно проверяться используемым валидатором.

**Дополнительное официальное представление:** [https://json-schema.org/draft/2020-12/json-schema-validation](https://json-schema.org/draft/2020-12/json-schema-validation).

<a id="S17"></a>
### S17. OpenAPI Specification 3.2.1 и 3.1.2

**Ссылка:** [https://spec.openapis.org/oas/v3.2.1.html](https://spec.openapis.org/oas/v3.2.1.html)

**Дата / версия / статус:** 3.2.1: 10.09.2026; для проекта выбран контракт 3.1.2.

**Тип:** Официальная спецификация.

**Что просмотрено:** Прочитаны обе опубликованные версии и разделение версии спецификации и API.

**Основание для архитектуры:** Формализованное описание HTTP API.

**Предел использования:** Выбор 3.1.2 — намеренное проектное решение для первичного инструментария, не утверждение, что это последняя версия.

**Дополнительное официальное представление:** [https://spec.openapis.org/oas/v3.1.2.html](https://spec.openapis.org/oas/v3.1.2.html).

<a id="S18"></a>
### S18. IETF. RFC 9457 — Problem Details for HTTP APIs

**Ссылка:** [https://www.rfc-editor.org/rfc/rfc9457.html](https://www.rfc-editor.org/rfc/rfc9457.html)

**Дата / версия / статус:** Июль 2023.

**Тип:** Открытый интернет-стандарт.

**Что просмотрено:** Прочитаны поля ответа об ошибке и ограничения раскрытия деталей.

**Основание для архитектуры:** Единый формат ошибок HTTP API.

**Предел использования:** Конкретные коды предметных ошибок в отчёте — проектные.

<a id="S19"></a>
### S19. IETF. RFC 9110 — HTTP Semantics

**Ссылка:** [https://www.rfc-editor.org/rfc/rfc9110.html](https://www.rfc-editor.org/rfc/rfc9110.html)

**Дата / версия / статус:** Июнь 2022.

**Тип:** Открытый интернет-стандарт.

**Что просмотрено:** Прочитаны относящиеся к проекту положения о 202 и условных запросах.

**Основание для архитектуры:** 202 Accepted не означает завершения; условное обновление версии ресурса.

**Предел использования:** Схема job/lease/idempotency — проектная реализация поверх HTTP, а не автоматическая гарантия RFC.

<a id="S20"></a>
### S20. PostgreSQL 18 — Row Security Policies

**Ссылка:** [https://www.postgresql.org/docs/18/ddl-rowsecurity.html](https://www.postgresql.org/docs/18/ddl-rowsecurity.html)

**Дата / версия / статус:** Документация ветки 18; проверка 18.10.2026.

**Тип:** Официальная документация.

**Что просмотрено:** Прочитаны политики RLS и исключения для владельца, superuser, BYPASSRLS.

**Основание для архитектуры:** Ограничения на уровне строк и условия обхода политик.

**Предел использования:** RLS не заменяет авторизацию приложения, безопасность файлов, индексов и процессов.

<a id="S21"></a>
### S21. PostgreSQL 18 — SELECT / SKIP LOCKED

**Ссылка:** [https://www.postgresql.org/docs/18/sql-select.html](https://www.postgresql.org/docs/18/sql-select.html)

**Дата / версия / статус:** Документация ветки 18; проверка 18.10.2026.

**Тип:** Официальная документация.

**Что просмотрено:** Прочитана семантика SKIP LOCKED и оговорка о queue-like tables.

**Основание для архитектуры:** Примитив для конкурентного получения задач из очереди.

**Предел использования:** Не готовый движок долговременных процессов и не гарантия exactly-once.

<a id="S22"></a>
### S22. pgvector — official repository and documentation

**Ссылка:** [https://github.com/pgvector/pgvector](https://github.com/pgvector/pgvector)

**Дата / версия / статус:** Изменяемая документация; проверка 18.10.2026.

**Тип:** Первичный репозиторий проекта.

**Что просмотрено:** Прочитаны exact/approximate search и фильтрация результатов индекса.

**Основание для архитектуры:** Векторный поиск в PostgreSQL; ограничения полноты при приближённом поиске с фильтрами.

**Предел использования:** В проекте не зафиксирована непроверенная версия расширения; безопасность и recall проверяются отдельно.

<a id="S23"></a>
### S23. FastAPI — Background Tasks

**Ссылка:** [https://fastapi.tiangolo.com/tutorial/background-tasks/](https://fastapi.tiangolo.com/tutorial/background-tasks/)

**Дата / версия / статус:** Изменяемая документация; проверка 18.10.2026.

**Тип:** Официальная документация.

**Что просмотрено:** Прочитан раздел Caveat о тяжёлых фоновых задачах.

**Основание для архитектуры:** Отделение простых задач после ответа от тяжёлых процессов.

**Предел использования:** BackgroundTasks не предлагается как долговременная очередь с восстановлением после сбоя.

<a id="S24"></a>
### S24. Pydantic — Strict mode

**Ссылка:** [https://docs.pydantic.dev/latest/concepts/strict_mode/](https://docs.pydantic.dev/latest/concepts/strict_mode/)

**Дата / версия / статус:** Изменяемая документация; проверка 18.10.2026.

**Тип:** Официальная документация.

**Что просмотрено:** Прочитан strict mode; исходный URL перенаправляет на текущую документацию.

**Основание для архитектуры:** Контроль приведения типов при проверке входа.

**Предел использования:** Strict mode имеет особенности для JSON и не заменяет предметные проверки единиц и научного смысла.

<a id="S25"></a>
### S25. OpenTelemetry — Signals

**Ссылка:** [https://opentelemetry.io/docs/concepts/signals/](https://opentelemetry.io/docs/concepts/signals/)

**Дата / версия / статус:** Изменяемая документация; проверка 18.10.2026.

**Тип:** Официальная документация.

**Что просмотрено:** Прочитано описание метрик, трассировок и журналов.

**Основание для архитектуры:** Техническая наблюдаемость приложения.

**Предел использования:** Трассировка не равна научному происхождению, аудиту решений или регуляторной валидации.

<a id="S26"></a>
### S26. OWASP Application Security Verification Standard

**Ссылка:** [https://owasp.org/projects/asvs](https://owasp.org/projects/asvs)

**Дата / версия / статус:** Стабильная редакция 5.0.0; 30.05.2025.

**Тип:** Открытый стандарт проверки безопасности сообщества OWASP.

**Что просмотрено:** Прочитаны страница проекта и сведения о релизе, не весь каталог требований.

**Основание для архитектуры:** Основание для явного плана проверок безопасности веб-приложения.

**Предел использования:** Соответствие ASVS не заявляется; нужен перечень применимых требований и реальные тесты.

**Дополнительное официальное представление:** [https://github.com/OWASP/ASVS/releases](https://github.com/OWASP/ASVS/releases).

<a id="S27"></a>
### S27. OWASP Top 10 for LLM Applications — LLM01:2025 Prompt Injection

**Ссылка:** [https://genai.owasp.org/llmrisk/llm01-prompt-injection/](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

**Дата / версия / статус:** Редакция 2025.

**Тип:** Первичная документация проекта безопасности.

**Что просмотрено:** Прочитаны механизмы prompt injection и ограничения мер защиты.

**Основание для архитектуры:** Внешние документы могут содержать управляющие инструкции; RAG сам по себе не устраняет риск.

**Предел использования:** Предлагаемые ограничения инструментов снижают риск, но не дают абсолютной защиты.

<a id="S28"></a>
### S28. OWASP — Server-Side Request Forgery Prevention Cheat Sheet

**Ссылка:** [https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)

**Дата / версия / статус:** Изменяемая документация; проверка 18.10.2026.

**Тип:** Первичная документация безопасности.

**Что просмотрено:** Прочитаны меры ограничения назначения сетевых запросов.

**Основание для архитектуры:** Контроль URL, IP, перенаправлений и доступа к внутренним ресурсам.

**Предел использования:** Проектная сетевая политика должна быть проверена тестами и инфраструктурой.

<a id="S29"></a>
### S29. OWASP — File Upload Cheat Sheet

**Ссылка:** [https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)

**Дата / версия / статус:** Изменяемая документация; проверка 18.10.2026.

**Тип:** Первичная документация безопасности.

**Что просмотрено:** Прочитаны ограничения типов, размера, размещения и обработки файлов.

**Основание для архитектуры:** Недоверенные файлы следует проверять и обрабатывать отдельно от привилегированной части системы.

**Предел использования:** Успешная проверка расширения или MIME не доказывает безопасность содержимого.

<a id="S30"></a>
### S30. NCBI PubChem — PUG REST and programmatic access

**Ссылка:** [https://pubchem.ncbi.nlm.nih.gov/pcfe/docs/markdown/pug-rest.md](https://pubchem.ncbi.nlm.nih.gov/pcfe/docs/markdown/pug-rest.md)

**Дата / версия / статус:** Изменяемая документация; проверка 18.10.2026.

**Тип:** Официальная документация API.

**Что просмотрено:** HTML PUG REST возвращал защитную страницу; прочитано полное официальное Markdown-представление.

**Основание для архитектуры:** Контракт PUG REST, ограничение запросов, throttling, обработка форматов и ошибок.

**Предел использования:** Документация прочитана; интеграционный прогон нового адаптера не выполнялся.

**Дополнительное официальное представление:** [https://pubchem.ncbi.nlm.nih.gov/docs/programmatic-access](https://pubchem.ncbi.nlm.nih.gov/docs/programmatic-access); [https://pubchem.ncbi.nlm.nih.gov/pcfe/docs/markdown/programmatic-access.md](https://pubchem.ncbi.nlm.nih.gov/pcfe/docs/markdown/programmatic-access.md).

<a id="S31"></a>
### S31. NCBI PubChem — PUG View

**Ссылка:** [https://pubchem.ncbi.nlm.nih.gov/pug_view/](https://pubchem.ncbi.nlm.nih.gov/pug_view/)

**Дата / версия / статус:** Изменяемая документация; проверка 18.10.2026.

**Тип:** Официальная документация API.

**Что просмотрено:** Прочитано назначение сервиса аннотаций.

**Основание для архитектуры:** Извлечение аннотаций и их происхождения отдельно от вычисленных свойств.

**Предел использования:** Аннотация агрегатора не превращается автоматически в независимое первичное измерение.

<a id="S32"></a>
### S32. DailyMed REST API v2 — /spls

**Ссылка:** [https://dailymed.nlm.nih.gov/dailymed/webservices-help/v2/spls_api.cfm](https://dailymed.nlm.nih.gov/dailymed/webservices-help/v2/spls_api.cfm)

**Дата / версия / статус:** API v2; проверка 18.10.2026.

**Тип:** Официальная документация NLM.

**Что просмотрено:** Прочитаны параметры поиска и формат результатов.

**Основание для архитектуры:** Продуктовые записи SPL и документированный доступ.

**Предел использования:** Не гарантируется полный количественный состав всех продуктов.

<a id="S33"></a>
### S33. DailyMed REST API v2 — SPL history

**Ссылка:** [https://dailymed.nlm.nih.gov/dailymed/webservices-help/v2/spls_setid_history_api.cfm](https://dailymed.nlm.nih.gov/dailymed/webservices-help/v2/spls_setid_history_api.cfm)

**Дата / версия / статус:** API v2; проверка 18.10.2026.

**Тип:** Официальная документация NLM.

**Что просмотрено:** Прочитана история версий по SETID.

**Основание для архитектуры:** Привязка к конкретной версии инструкции.

**Предел использования:** Одна ссылка на актуальную страницу не заменяет снимок использованной версии.

<a id="S34"></a>
### S34. ChEMBL — Data Web Services

**Ссылка:** [https://chembl.gitbook.io/chembl-interface-documentation/web-services/chembl-data-web-services](https://chembl.gitbook.io/chembl-interface-documentation/web-services/chembl-data-web-services)

**Дата / версия / статус:** Изменяемая документация; проверка 18.10.2026.

**Тип:** Официальная документация EMBL-EBI.

**Что просмотрено:** Прочитана документация; Swagger-страница отдельно отдавала только JS-оболочку.

**Основание для архитектуры:** Сущности API, пагинация page_meta и переход по next.

**Предел использования:** Нельзя объявлять первую страницу полной выгрузкой; контекст assay сохраняется.

<a id="S35"></a>
### S35. RDKit — MolStandardize API

**Ссылка:** [https://www.rdkit.org/docs/source/rdkit.Chem.MolStandardize.rdMolStandardize.html](https://www.rdkit.org/docs/source/rdkit.Chem.MolStandardize.rdMolStandardize.html)

**Дата / версия / статус:** Документация 2026.09.1 на момент просмотра.

**Тип:** Официальная документация.

**Что просмотрено:** Прочитаны операции нормализации и FragmentParent.

**Основание для архитектуры:** Доступные операции химической стандартизации.

**Предел использования:** Удаление фрагментов меняет представление соли/комплекса; исходник и преобразования необходимо сохранять.

<a id="S36"></a>
### S36. FDA — Inactive Ingredients in Approved Drug Products: FAQ

**Ссылка:** [https://www.fda.gov/drugs/drug-approvals-and-databases/inactive-ingredients-approved-drug-products-search-frequently-asked-questions](https://www.fda.gov/drugs/drug-approvals-and-databases/inactive-ingredients-approved-drug-products-search-frequently-asked-questions)

**Дата / версия / статус:** Динамическая официальная документация; проверка 18.10.2026.

**Тип:** Регуляторная база и её пояснение.

**Что просмотрено:** Прочитаны пояснения maximum potency и maximum daily exposure.

**Основание для архитектуры:** Прецеденты эксципиентов с контекстом пути и формы.

**Предел использования:** Не универсальная таблица разрешённых безопасных доз; отсутствие записи не равно запрету.

<a id="S37"></a>
### S37. openFDA — Drug Adverse Events

**Ссылка:** [https://open.fda.gov/apis/drug/event/](https://open.fda.gov/apis/drug/event/)

**Дата / версия / статус:** Динамическая документация; проверка 18.10.2026.

**Тип:** Официальная документация FDA.

**Что просмотрено:** Прочитаны ограничения интерпретации.

**Основание для архитектуры:** Сообщения о нежелательных событиях и их использование для поиска сигналов.

**Предел использования:** Нельзя по одному подсчёту сообщений устанавливать причинность, частоту или эффективность сочетаний.

<a id="S38"></a>
### S38. FDA — Orange Book

**Ссылка:** [https://www.fda.gov/drugs/drug-approvals-and-databases/approved-drug-products-therapeutic-equivalence-evaluations-orange-book](https://www.fda.gov/drugs/drug-approvals-and-databases/approved-drug-products-therapeutic-equivalence-evaluations-orange-book)

**Дата / версия / статус:** Динамический реестр; проверка 18.10.2026.

**Тип:** Официальный источник FDA.

**Что просмотрено:** Прочитана официальная страница.

**Основание для архитектуры:** Продукты, терапевтическая эквивалентность, перечисленные патенты и эксклюзивность.

**Предел использования:** Не полное заключение о патентной свободе в любой юрисдикции.

<a id="S39"></a>
### S39. Государственный реестр лекарственных средств РФ

**Ссылка:** [https://grls.minzdrav.gov.ru/](https://grls.minzdrav.gov.ru/)

**Дата / версия / статус:** Динамический реестр; проверка 18.10.2026.

**Тип:** Официальный реестр.

**Что просмотрено:** Прочитана доступная официальная страница.

**Основание для архитектуры:** Российские регистрационные сведения и инструкции.

**Предел использования:** Публичный промышленный API не подтверждён. Предлагается контролируемый импорт при отсутствии проверенного контракта.

<a id="S40"></a>
### S40. Europe PMC — RESTful Web Service

**Ссылка:** [https://europepmc.org/RestfulWebService](https://europepmc.org/RestfulWebService)

**Дата / версия / статус:** Документация API; проверка 18.10.2026.

**Тип:** Официальная документация литературного сервиса.

**Что просмотрено:** Прямое открытие завершалось ошибкой доступа; доступно индексированное описание официального источника.

**Основание для архитектуры:** Назначение поиска метаданных и доступного полного текста.

**Предел использования:** Успешный запрос production API и полнотекстовые права каждой статьи в этом этапе не проверены; требуется интеграционный тест.

<a id="S41"></a>
### S41. Fu et al. ADMETlab 3.0

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/38572755/](https://pubmed.ncbi.nlm.nih.gov/38572755/)

**Дата / версия / статус:** 2024; Nucleic Acids Research.

**Тип:** Первичная научная публикация разработчиков.

**Что просмотрено:** Библиографическое описание/аннотация, использованные также в этапе 2; текущая страница ограниченно отдаёт текст.

**Основание для архитектуры:** Наличие ADMET-предикторов, программного доступа и оценок неопределённости в публикации.

**Предел использования:** Текущий контракт API, SLA и право коммерческой интеграции не установлены одной статьёй.

<a id="S42"></a>
### S42. Open Systems Pharmacology — OSPSuite-R

**Ссылка:** [https://www.open-systems-pharmacology.org/OSPSuite-R/](https://www.open-systems-pharmacology.org/OSPSuite-R/)

**Дата / версия / статус:** Действующая документация; проверка 18.10.2026.

**Тип:** Официальная техническая документация.

**Что просмотрено:** Прочитаны назначение пакета, запуск симуляций и зависимости.

**Основание для архитектуры:** Загрузка и выполнение моделей PK-Sim/MoBi из R.

**Предел использования:** Совместимость конкретного runner-image с моделями необходимо проверять; не приписывается одинаковая поддержка всем GUI и workflow.

<a id="S43"></a>
### S43. Open Systems Pharmacology — Qualification workflow

**Ссылка:** [https://docs.open-systems-pharmacology.org/shared-tools-and-example-workflows/qualification](https://docs.open-systems-pharmacology.org/shared-tools-and-example-workflows/qualification)

**Дата / версия / статус:** Действующая документация; проверка 18.10.2026.

**Тип:** Официальная документация.

**Что просмотрено:** Прочитаны планы, наблюдения, запуск и отчёт квалификации.

**Основание для архитектуры:** Воспроизводимый контур проверки моделей в заданном сценарии.

**Предел использования:** Документация ограничивает поддерживаемые типы проектов; поддержка MoBi в других компонентах не означает автоматическую поддержку данного workflow.

<a id="S44"></a>
### S44. MolecularAI — AiZynthFinder

**Ссылка:** [https://github.com/MolecularAI/aizynthfinder](https://github.com/MolecularAI/aizynthfinder)

**Дата / версия / статус:** Изменяемый первичный репозиторий; проверка 18.10.2026.

**Тип:** Код и документация разработчиков.

**Что просмотрено:** Прочитаны назначение, конфигурации и условия лицензии кода.

**Основание для архитектуры:** Ретросинтетический поиск, модели и исходные вещества как отдельные входы.

**Предел использования:** MIT кода не определяет автоматически права всех весов/данных и не подтверждает практический синтез.

<a id="S45"></a>
### S45. OECD. (Q)SAR Assessment Framework, Second Edition

**Ссылка:** [https://www.oecd.org/en/publications/q-sar-assessment-framework-guidance-for-the-regulatory-assessment-of-quantitative-structure-activity-relationship-models-and-predictions-second-edition_bbdac345-en.html](https://www.oecd.org/en/publications/q-sar-assessment-framework-guidance-for-the-regulatory-assessment-of-quantitative-structure-activity-relationship-models-and-predictions-second-edition_bbdac345-en.html)

**Дата / версия / статус:** Второе издание; 15.11.2024; DOI 10.1787/bbdac345-en.

**Тип:** Руководство OECD.

**Что просмотрено:** Прочитана официальная аннотация, не полный многостраничный текст.

**Основание для архитектуры:** Раздельная оценка модели, отдельного прогноза и совокупности прогнозов.

**Предел использования:** Не заявляется полное прохождение QAF будущими предикторами.

<a id="S46"></a>
### S46. FDA. Liposome Drug Products: CMC; Human Pharmacokinetics and Bioavailability; Labeling

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/liposome-drug-products-chemistry-manufacturing-and-controls-human-pharmacokinetics-and](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/liposome-drug-products-chemistry-manufacturing-and-controls-human-pharmacokinetics-and)

**Дата / версия / статус:** Final; апрель 2018.

**Тип:** Специализированное регуляторное руководство.

**Что просмотрено:** Прочитана официальная карточка и область применения.

**Основание для архитектуры:** Специфичность сложных систем доставки и необходимости CMC/PK-данных.

**Предел использования:** Не общий универсальный протокол для всех парентеральных форм.

<a id="S47"></a>
### S47. ChEMBL Structure Pipeline

**Ссылка:** [https://github.com/chembl/ChEMBL_Structure_Pipeline](https://github.com/chembl/ChEMBL_Structure_Pipeline)

**Дата / версия / статус:** Изменяемый первичный репозиторий; проверка 18.10.2026.

**Тип:** Код и документация EMBL-EBI.

**Что просмотрено:** Прочитано разделение checker, standardizer и getParent.

**Основание для архитектуры:** Поэтапная химическая проверка и нормализация, а не одно недокументированное преобразование.

**Предел использования:** Получение родительской структуры не устанавливает идентичность конечного продукта.

