# Реестр источников к этапу 1 дипломного проекта

**Тема:** ИИ-платформа оптимизации всасывания и лекарственной формы препаратов.

**Дата проверки:** 17 октября 2026 года.

Это аннотированный реестр использованных и рассмотренных источников, а не заявление о проведённом систематическом обзоре всей литературы. Главы отчёта представлены в ответе в чате. Официальные страницы устанавливают содержание и статус регуляторных документов; статьи — результаты конкретных исследований; страницы производителей — только заявленные функции продуктов. Даты публикации и обновления не подменяются датой обращения. Для материалов с доступной только аннотацией не заявляется чтение полного протокола. Прямой доступ к отдельной странице может зависеть от региона, JavaScript и защиты сайта.

Исходное ТЗ: предоставленный пользователем файл `DESCR(1).md`; это источник требований проекта, а не доказательство научных утверждений.

## R01. FDA Inactive Ingredient Database (IID)

**Ссылка:** [https://www.accessdata.fda.gov/scripts/cder/iig/index.cfm](https://www.accessdata.fda.gov/scripts/cder/iig/index.cfm)

**Дата / версия:** Данные по 29.05.2026; обновление интерфейса базы 23.07.2026.

**Тип источника:** Официальная база FDA.

**Что подтверждает:** Прецеденты использования вспомогательных веществ по пути введения и форме.

**Ограничение:** Не является универсальным разрешением безопасности; дата обращения не равна дате данных.

## R02. FDA: Inactive Ingredients — Frequently Asked Questions

**Ссылка:** [https://www.fda.gov/drugs/drug-approvals-and-databases/inactive-ingredients-approved-drug-products-search-frequently-asked-questions](https://www.fda.gov/drugs/drug-approvals-and-databases/inactive-ingredients-approved-drug-products-search-frequently-asked-questions)

**Дата / версия:** Динамическая документация; проверена 17.10.2026.

**Тип источника:** Официальная документация.

**Что подтверждает:** Объяснения maximum potency и maximum daily exposure.

**Ограничение:** Разовая дозировочная единица и суточная экспозиция — разные показатели.

## R03. FDA: Questions & Answers Regarding Enhancements to IID

**Ссылка:** [https://www.fda.gov/drugs/drug-approvals-and-databases/questions-answers-regarding-enhancements-inactive-ingredient-database-iid](https://www.fda.gov/drugs/drug-approvals-and-databases/questions-answers-regarding-enhancements-inactive-ingredient-database-iid)

**Дата / версия:** Проверено 17.10.2026.

**Тип источника:** Официальная документация.

**Что подтверждает:** Оговорки о происхождении значений potency и MDE.

**Ограничение:** Показатели могут относиться к разным продуктам.

## R04. FDA Orange Book

**Ссылка:** [https://www.fda.gov/drugs/drug-approvals-and-databases/approved-drug-products-therapeutic-equivalence-evaluations-orange-book](https://www.fda.gov/drugs/drug-approvals-and-databases/approved-drug-products-therapeutic-equivalence-evaluations-orange-book)

**Дата / версия:** Динамическая база; проверена 17.10.2026.

**Тип источника:** Официальная база FDA.

**Что подтверждает:** Одобрения, терапевтическая эквивалентность, перечисленные патенты и эксклюзивность.

**Ограничение:** Не заключение о свободе использования разработки во всех юрисдикциях.

## R05. DailyMed

**Ссылка:** [https://dailymed.nlm.nih.gov/](https://dailymed.nlm.nih.gov/)

**Дата / версия:** Динамическая база; проверена 17.10.2026.

**Тип источника:** NLM, инструкции SPL.

**Что подтверждает:** Идентификация конкретного продукта, инструкции, состав, версии маркировки.

**Ограничение:** Наличие записи не делает любое изделие одобренным FDA; количества всех эксципиентов могут отсутствовать.

## R06. Государственный реестр лекарственных средств РФ

**Ссылка:** [https://grls.minzdrav.gov.ru/](https://grls.minzdrav.gov.ru/)

**Дата / версия:** Проверено 17.10.2026; на странице видны сообщения октября 2026.

**Тип источника:** Официальный реестр.

**Что подтверждает:** Российские регистрационные сведения и инструкции.

**Ограничение:** Публичный API и возможность промышленной выгрузки в этом исследовании не подтверждены.

## R07. openFDA: Drug Adverse Events

**Ссылка:** [https://open.fda.gov/apis/drug/event/](https://open.fda.gov/apis/drug/event/)

**Дата / версия:** Динамическая документация; проверена 17.10.2026.

**Тип источника:** Официальная документация FDA.

**Что подтверждает:** Открытые сообщения о нежелательных событиях и ограничения интерпретации.

**Ограничение:** Нельзя устанавливать причинность или рассчитывать частоту осложнений по одним числам сообщений.

## R08. PubChem

**Ссылка:** [https://pubchem.ncbi.nlm.nih.gov/](https://pubchem.ncbi.nlm.nih.gov/)

**Дата / версия:** Динамическая база; проверена 17.10.2026.

**Тип источника:** NCBI/NIH.

**Что подтверждает:** Химические идентификаторы, структуры и сведения из разных источников.

**Ограничение:** Главная страница зависит от JavaScript; содержательная проверка дополнена статьёй PubChem 2025.

## R09. ChEMBL

**Ссылка:** [https://www.ebi.ac.uk/chembl/](https://www.ebi.ac.uk/chembl/)

**Дата / версия:** Динамическая база; проверена 17.10.2026.

**Тип источника:** EMBL-EBI.

**Что подтверждает:** Биоактивность и экспериментальные измерения с контекстом анализа.

**Ограничение:** Не единая база готовых рецептур и не справочник гарантированных клинических эффектов.

## R10. SwissADME

**Ссылка:** [https://www.swissadme.ch/](https://www.swissadme.ch/)

**Дата / версия:** Проверено 17.10.2026; статья метода — 2017.

**Тип источника:** Официальный инструмент разработчиков.

**Что подтверждает:** Оценки физико-химических и ADME-свойств.

**Ограничение:** Прогнозы не равны измерениям; текущий сервис мог измениться относительно статьи. Промышленный API не проверялся.

## R11. ADMETlab 3.0

**Ссылка:** [https://admetlab3.scbdd.com/](https://admetlab3.scbdd.com/)

**Дата / версия:** Версия 3.0; на сайте дата 31.01.2024; статья — 2024.

**Тип источника:** Официальный инструмент разработчиков.

**Что подтверждает:** Предсказательные модели ADMET, API, оценки неопределённости.

**Ограничение:** Доступность сайта не доказывает пригодность конкретной модели для неизвестной химической области.

## R12. Open Systems Pharmacology / PK-Sim

**Ссылка:** [https://www.open-systems-pharmacology.org/](https://www.open-systems-pharmacology.org/)

**Дата / версия:** Динамический проект; проверен 17.10.2026.

**Тип источника:** Официальный открытый проект.

**Что подтверждает:** Механистическое физиологически обоснованное фармакокинетическое моделирование.

**Ограничение:** Конкретную модель требуется параметризовать и валидировать; открытость ПО не подтверждает правильность любого расчёта.

## R13. Therapeutics Data Commons

**Ссылка:** [https://tdcommons.ai/](https://tdcommons.ai/)

**Дата / версия:** Динамический проект; проверен 17.10.2026.

**Тип источника:** Официальный научный проект.

**Что подтверждает:** Датасеты, задачи и инструменты оценки моделей.

**Ограничение:** Готовый универсальный эталон оптимальных лекарственных форм этим не подтверждён.

## R14. Europe PMC RESTful Web Service

**Ссылка:** [https://europepmc.org/RestfulWebService](https://europepmc.org/RestfulWebService)

**Дата / версия:** Проверено 17.10.2026.

**Тип источника:** Официальная документация API.

**Что подтверждает:** Поиск публикаций и метаданных, работа с доступными полнотекстовыми материалами.

**Ограничение:** Прямое открытие документации получило HTTP 403; сведения подтверждены индексированной официальной документацией. Успешная интеграция API не заявляется.

## R15. ICH Quality Guidelines

**Ссылка:** [https://www.ich.org/page/quality-guidelines](https://www.ich.org/page/quality-guidelines)

**Дата / версия:** Проверено 17.10.2026.

**Тип источника:** Официальный каталог.

**Что подтверждает:** Навигация по руководствам серии Q.

**Ограничение:** Каталог не отдал читаемый текст; содержание и статус конкретных документов сверялись через FDA/EMA.

## R16. Amidon et al. A theoretical basis for a biopharmaceutic drug classification

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/7617530/](https://pubmed.ncbi.nlm.nih.gov/7617530/)

**Дата / версия:** 1995; Pharm Res 12(3):413–420; DOI 10.1023/A:1016212804288.

**Тип источника:** Фундаментальная научная статья.

**Что подтверждает:** Теоретическая основа BCS: растворимость, проницаемость и растворение.

**Ограничение:** Не актуальное руководство по регуляторному освобождению от исследований.

## R17. Savjani et al. Drug Solubility: Importance and Enhancement Techniques

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/22830056/](https://pubmed.ncbi.nlm.nih.gov/22830056/)

**Дата / версия:** 2012; ISRN Pharmaceutics:195727; DOI 10.5402/2012/195727.

**Тип источника:** Обзор.

**Что подтверждает:** Классификация методов изменения растворимости.

**Ограничение:** Исторический обзор, не источник современной доли нерастворимых кандидатов или гарантии действия стратегии.

## R18. Serajuddin. Salt formation to improve drug solubility

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/17619064/](https://pubmed.ncbi.nlm.nih.gov/17619064/)

**Дата / версия:** 2007; Adv Drug Deliv Rev 59(7):603–616; DOI 10.1016/j.addr.2007.05.010.

**Тип источника:** Механистический обзор.

**Что подтверждает:** Условия солеобразования и растворимости солей.

**Ограничение:** Разность pKa — не достаточное доказательство пригодности соли.

## R19. Paulekuhn, Dressman, Saal. Trends in Active Pharmaceutical Ingredient Salt Selection

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/18052022/](https://pubmed.ncbi.nlm.nih.gov/18052022/)

**Дата / версия:** 2007; J Med Chem 50(26):6665–6672; DOI 10.1021/jm701032y.

**Тип источника:** Первичное исследование базы Orange Book.

**Что подтверждает:** Исторические закономерности выбора противоионов.

**Ограничение:** Результаты 2007 года нельзя подписывать как статистику 2026 года.

## R20. FDA ICH M9: BCS-Based Biowaivers

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m9-biopharmaceutics-classification-system-based-biowaivers](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m9-biopharmaceutics-classification-system-based-biowaivers)

**Дата / версия:** Final, май 2021.

**Тип источника:** Официальное руководство.

**Что подтверждает:** Область применения BCS-биовейвера и требования к доказательствам.

**Ограничение:** Не даёт права присвоить регуляторный BCS по одному in silico прогнозу. PDF: https://www.fda.gov/media/148472/download

## R21. FDA ICH M13A: Bioequivalence for Immediate-Release Solid Oral Dosage Forms

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m13a-bioequivalence-immediate-release-solid-oral-dosage-forms](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m13a-bioequivalence-immediate-release-solid-oral-dosage-forms)

**Дата / версия:** Final, октябрь 2024.

**Тип источника:** Официальное руководство.

**Что подтверждает:** Исследования биоэквивалентности форм в области действия документа.

**Ограничение:** Пределы 80–125% относятся к соответствующим отношениям PK-параметров и доверительным интервалам, не к содержанию таблетки. PDF: https://www.fda.gov/media/165049/download

## R22. FDA ICH Q8(R2): Pharmaceutical Development

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q8r2-pharmaceutical-development](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q8r2-pharmaceutical-development)

**Дата / версия:** Final, ноябрь 2009.

**Тип источника:** Официальное руководство.

**Что подтверждает:** QTPP, показатели качества, состав и процесс разработки.

**Ограничение:** Рамочная методология, не готовая рецептура. PDF: https://www.fda.gov/media/71535/download

## R23. FDA ICH Q9(R1): Quality Risk Management

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q9r1-quality-risk-management](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q9r1-quality-risk-management)

**Дата / версия:** Final, май 2023.

**Тип источника:** Официальное руководство.

**Что подтверждает:** Управление рисками качества и субъективностью оценки.

**Ограничение:** Не заменяет экспериментальное подтверждение качества.

## R24. FDA ICH Q1A(R2): Stability Testing

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q1ar2-stability-testing-new-drug-substances-and-products](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q1ar2-stability-testing-new-drug-substances-and-products)

**Дата / версия:** Final, ноябрь 2003.

**Тип источника:** Официальное руководство.

**Что подтверждает:** Испытания стабильности.

**Ограничение:** Применимость условий зависит от продукта, упаковки и рынка; не следует смешивать с проектом нового Q1.

## R25. EMA: consolidated ICH Q1 guideline

**Ссылка:** [https://www.ema.europa.eu/en/scientific-guidelines/ich-q1-guideline-stability-testing-drug-substances-drug-products](https://www.ema.europa.eu/en/scientific-guidelines/ich-q1-guideline-stability-testing-drug-substances-drug-products)

**Дата / версия:** Step 2b draft; опубликован 30.04.2025; статус проверен 17.10.2026.

**Тип источника:** Проект официального руководства.

**Что подтверждает:** Проект консолидации руководств стабильности.

**Ограничение:** На проверенной странице отмечен Draft, а не окончательно внедрённая замена Q1A-F/Q5C.

## R26. FDA: Determining Whether to Submit an ANDA or a 505(b)(2) Application

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/determining-whether-submit-anda-or-505b2-application](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/determining-whether-submit-anda-or-505b2-application)

**Дата / версия:** Final, май 2019.

**Тип источника:** Официальное руководство.

**Что подтверждает:** Различие сокращённых регистрационных путей США.

**Ограничение:** Выбор пути зависит от конкретного продукта и данных.

## R27. FDA: ANDA or 505(b)(2), proposed revision

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/determining-whether-submit-anda-or-505b2-application-0](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/determining-whether-submit-anda-or-505b2-application-0)

**Дата / версия:** Draft, август 2026; комментарии до 19.10.2026.

**Тип источника:** Проект официального руководства.

**Что подтверждает:** Актуальный проект пересмотра документа 2019 года.

**Ограничение:** Прямо указано, что заменит версию 2019 года только после финализации.

## R28. FDA: Regulatory Classification of Pharmaceutical Co-Crystals

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/regulatory-classification-pharmaceutical-co-crystals](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/regulatory-classification-pharmaceutical-co-crystals)

**Дата / версия:** Final, февраль 2018.

**Тип источника:** Официальное руководство.

**Что подтверждает:** Отдельное регуляторное рассмотрение сокристаллов.

**Ограничение:** Нельзя автоматически считать любую твёрдофазную модификацию новой ковалентной молекулой.

## R29. FDA: PBPK Analyses — Biopharmaceutics Applications for Oral Drug Product Development

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/use-physiologically-based-pharmacokinetic-analyses-biopharmaceutics-applications-oral-drug-product](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/use-physiologically-based-pharmacokinetic-analyses-biopharmaceutics-applications-oral-drug-product)

**Дата / версия:** Draft, сентябрь 2020.

**Тип источника:** Проект официального руководства.

**Что подтверждает:** Применение PBPK/PBBM в разработке пероральных форм.

**Ограничение:** Проект, не универсальное разрешение заменить клинические исследования моделированием.

## R30. FDA: AI to Support Regulatory Decision-Making for Drug and Biological Products

**Ссылка:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological)

**Дата / версия:** Draft, январь 2025; статус проверен 17.10.2026.

**Тип источника:** Проект официального руководства.

**Что подтверждает:** Контекст использования и риск-ориентированная оценка доверия к модели.

**Ограничение:** Не действующее обязательное правило для любого исследовательского чат-бота.

## R31. EMA: Pharmaceutical development of medicines for paediatric use

**Ссылка:** [https://www.ema.europa.eu/en/scientific-guidelines/pharmaceutical-development-medicines-paediatric-use](https://www.ema.europa.eu/en/scientific-guidelines/pharmaceutical-development-medicines-paediatric-use)

**Дата / версия:** Rev. 2, 31.07.2013; current effective version на проверенной странице.

**Тип источника:** Официальное руководство.

**Что подтверждает:** Возрастная пригодность лекарственной формы.

**Ограничение:** Педиатрическую пригодность нельзя выводить только из взрослого прецедента использования.

## R32. Varma et al. Physicochemical Space for Optimum Oral Bioavailability

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/20070106/](https://pubmed.ncbi.nlm.nih.gov/20070106/)

**Дата / версия:** 2010; J Med Chem 53(3):1098–1108; DOI 10.1021/jm901371v.

**Тип источника:** Первичное исследование.

**Что подтверждает:** Разделение Fa, Fg, Fh и системной биодоступности.

**Ограничение:** Физико-химические корреляции не заменяют измерение конкретной формы.

## R33. Takahashi et al. Human absorption and intestinal metabolism of cobimetinib

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/26451002/](https://pubmed.ncbi.nlm.nih.gov/26451002/)

**Дата / версия:** Онлайн 08.10.2015; выпуск январь 2016; DOI 10.1124/dmd.115.066282.

**Тип источника:** Первичное исследование у людей.

**Что подтверждает:** Хорошее всасывание при существенно меньшей системной биодоступности.

**Ограничение:** Fg оценивали с модельными предположениями; пример не универсален.

## R34. Soul-Lawton et al. Absolute bioavailability of valaciclovir

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/8593015/](https://pubmed.ncbi.nlm.nih.gov/8593015/)

**Дата / версия:** 1995; AAC 39(12):2759–2764; DOI 10.1128/AAC.39.12.2759.

**Тип источника:** Рандомизированное перекрёстное PK-исследование.

**Что подтверждает:** 12 добровольцев; средняя абсолютная биодоступность ацикловира из валацикловира 54,2%.

**Ограничение:** Результат конкретного исследования, не прогноз для любого аминокислотного пролекарства; использована аннотация.

## R35. Ganapathy et al. Valacyclovir: a substrate for PEPT1 and PEPT2

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/9610386/](https://pubmed.ncbi.nlm.nih.gov/9610386/)

**Дата / версия:** 1998; DOI 10.1006/bbrc.1998.8628.

**Тип источника:** Первичное клеточное/транспортное исследование.

**Что подтверждает:** Подтверждение взаимодействия пролекарства с переносчиками.

**Ограничение:** Клеточная модель не равна клиническому исследованию эффективности.

## R36. Bauer et al. Ritonavir: An Extraordinary Example of Conformational Polymorphism

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/11474792/](https://pubmed.ncbi.nlm.nih.gov/11474792/)

**Дата / версия:** 2001; Pharm Res 18(6):859–866; DOI 10.1023/A:1011052932607.

**Тип источника:** Первичное исследование промышленного случая.

**Что подтверждает:** Проблема новой менее растворимой кристаллической формы ритонавира.

**Ограничение:** Исторический случай, а не частота всех промышленных неудач.

## R37. Iuzzolino et al. Predicting the ritonavir crisis by revisiting the polymorph landscape

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/41429893/](https://pubmed.ncbi.nlm.nih.gov/41429893/)

**Дата / версия:** 22.12.2025; Commun Chem 8:404; DOI 10.1038/s42004-025-01814-6.

**Тип источника:** Первичное вычислительно-структурное исследование.

**Что подтверждает:** Ретроспективный анализ полиморфного ландшафта.

**Ограничение:** Не проспективная гарантия предотвращения кризисов и не доказательство силы одной LLM.

## R38. Buckley et al. Transcellular stomach absorption of a derivatized GLP-1 receptor agonist

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/30429357/](https://pubmed.ncbi.nlm.nih.gov/30429357/)

**Дата / версия:** 14.11.2018; Sci Transl Med 10:eaar7047; DOI 10.1126/scitranslmed.aar7047.

**Тип источника:** Первичное клиническое/доклиническое исследование.

**Что подтверждает:** Механизм перорального семаглутида с SNAC.

**Ограничение:** Не доказательство переносимости механизма на любой пептид.

## R39. DailyMed: Itraconazole capsules, Alembic

**Ссылка:** [https://www.dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=23126370-8d6a-4027-bd8f-860e2776ba3a](https://www.dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=23126370-8d6a-4027-bd8f-860e2776ba3a)

**Дата / версия:** Обновление 17.09.2026.

**Тип источника:** Инструкция конкретного продукта.

**Что подтверждает:** Пищевой/кислотностный эффект и невзаимозаменяемость капсул с раствором.

**Ограничение:** Нельзя переносить указания капсул на все формы итраконазола.

## R40. Yu et al. Understanding excipient-induced crystallization of spray-dried amorphous solid dispersion

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/39306037/](https://pubmed.ncbi.nlm.nih.gov/39306037/)

**Дата / версия:** Онлайн 19.09.2024; J Pharm Sci 2025;114:234–244; DOI 10.1016/j.xphs.2024.08.024.

**Тип источника:** Первичное экспериментальное исследование.

**Что подтверждает:** Тип эксципиента и характер контакта влияют на рекристаллизацию модельной системы.

**Ограничение:** Вывод относится к изученной системе; использована аннотация, не все экспериментальные приложения.

## R41. Daina, Michielin, Zoete. SwissADME

**Ссылка:** [https://www.nature.com/articles/srep42717](https://www.nature.com/articles/srep42717)

**Дата / версия:** 03.03.2017; Scientific Reports 7:42717; DOI 10.1038/srep42717.

**Тип источника:** Статья разработчиков метода.

**Что подтверждает:** Устройство и ограничения предикторов SwissADME.

**Ограничение:** Bioavailability Score нельзя трактовать как процент биодоступности у человека.

## R42. Fu et al. ADMETlab 3.0

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/38572755/](https://pubmed.ncbi.nlm.nih.gov/38572755/)

**Дата / версия:** 2024; NAR 52(W1):W422–W431; DOI 10.1093/nar/gkae236.

**Тип источника:** Статья разработчиков метода.

**Что подтверждает:** Предсказания ADMET, 119 характеристик и оценка неопределённости.

**Ограничение:** 119 характеристик не означают 119 независимых клинически валидированных исходов.

## R43. Kim et al. PubChem 2025 update

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/39558165/](https://pubmed.ncbi.nlm.nih.gov/39558165/)

**Дата / версия:** Онлайн 18.11.2024; NAR 2025;53:D1516–D1525; DOI 10.1093/nar/gkae1059.

**Тип источника:** Статья разработчиков базы.

**Что подтверждает:** Источники и развитие PubChem.

**Ограничение:** Год выпуска статьи не фиксирует состояние динамической базы на октябрь 2026.

## R44. The ChEMBL Database in 2023

**Ссылка:** [https://academic.oup.com/nar/article/52/D1/D1180/7337608](https://academic.oup.com/nar/article/52/D1/D1180/7337608)

**Дата / версия:** Онлайн 02.11.2023; NAR 2024;52:D1180–D1192; DOI 10.1093/nar/gkad1004.

**Тип источника:** Статья разработчиков базы.

**Что подтверждает:** Разные типы биоактивности и происхождение данных.

**Ограничение:** Историческое описание выпуска, не обещание полного набора рецептур.

## R45. GastroPlus

**Ссылка:** [https://www.simulations-plus.com/software/gastroplus/](https://www.simulations-plus.com/software/gastroplus/)

**Дата / версия:** Текущая страница проверена 17.10.2026.

**Тип источника:** Документация производителя.

**Что подтверждает:** PBPK/PBBM, модели абсорбции, автоматизация и заявленные AI-функции.

**Ограничение:** Подтверждает заявленные возможности, не независимую величину экономии или точности.

## R46. Simcyp Biopharmaceutics

**Ссылка:** [https://www.certara.com/software/simcyp-biopharmaceutics/](https://www.certara.com/software/simcyp-biopharmaceutics/)

**Дата / версия:** Текущая страница проверена 17.10.2026.

**Тип источника:** Документация производителя.

**Что подтверждает:** Моделирование абсорбции и биофармацевтических сценариев.

**Ограничение:** Независимый сравнительный тест в рамках этого отчёта не проводился.

## R47. BASF ZoomLab

**Ссылка:** [https://pharmaceutical.basf.com/global/en/pharma-solutions/about-basf-pharma/digitalization/zoomlab](https://pharmaceutical.basf.com/global/en/pharma-solutions/about-basf-pharma/digitalization/zoomlab)

**Дата / версия:** Текущая страница проверена 17.10.2026.

**Тип источника:** Документация производителя.

**Что подтверждает:** Цифровая поддержка разработки лекарственной формы и выбора ингредиентов.

**Ограничение:** Заявления поставщика не равны доказательству оптимальности для всего рынка.

## R48. Saigiridharan et al. AiZynthFinder 4.0

**Ссылка:** [https://link.springer.com/article/10.1186/s13321-024-00860-x](https://link.springer.com/article/10.1186/s13321-024-00860-x)

**Дата / версия:** 23.05.2024; J Cheminform 16:57; DOI 10.1186/s13321-024-00860-x.

**Тип источника:** Первичное описание ПО и промышленного применения.

**Что подтверждает:** Алгоритмы ретросинтеза, поиск и оценка маршрутов.

**Ограничение:** Маршрут до доступных прекурсоров не равен лабораторно подтверждённому выходу и масштабированию.

## R49. Lu et al. HTS and ML for binary and ternary ASD formation

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/40180767/](https://pubmed.ncbi.nlm.nih.gov/40180767/)

**Дата / версия:** 03.04.2025; Pharm Res 42:697–709; DOI 10.1007/s11095-025-03853-z.

**Тип источника:** Первичное экспериментальное ML-исследование.

**Что подтверждает:** 1272 композиции; классификация образования ASD; accuracy 96,7%, F1 83,6%.

**Ограничение:** Исход — аморфное состояние по PXRD, не клиническая биодоступность; выводы взяты из опубликованной аннотации.

## R50. Bran et al. Augmenting large language models with chemistry tools (ChemCrow)

**Ссылка:** [https://www.nature.com/articles/s42256-024-00832-8](https://www.nature.com/articles/s42256-024-00832-8)

**Дата / версия:** 08.05.2024; Nature Machine Intelligence 6:525–535; DOI 10.1038/s42256-024-00832-8.

**Тип источника:** Первичная исследовательская работа.

**Что подтверждает:** Интеграция LLM с химическими инструментами.

**Ограничение:** Не валидация данной дипломной платформы и не клиническая оценка лекарственной формы.

## R51. Gao et al. Enabling Large Language Models to Generate Text with Citations (ALCE)

**Ссылка:** [https://aclanthology.org/2023.emnlp-main.398/](https://aclanthology.org/2023.emnlp-main.398/)

**Дата / версия:** EMNLP, декабрь 2023; DOI 10.18653/v1/2023.emnlp-main.398.

**Тип источника:** Первичная исследовательская работа.

**Что подтверждает:** Отдельная оценка качества ответа и качества цитирования.

**Ограничение:** Исторические результаты моделей не являются частотами ошибок моделей 2026 года.

## R52. TDC: Dataset Splits

**Ссылка:** [https://tdcommons.ai/functions/data_split/](https://tdcommons.ai/functions/data_split/)

**Дата / версия:** Динамическая документация; проверена 17.10.2026.

**Тип источника:** Официальная документация научного проекта.

**Что подтверждает:** Scaffold split и другие способы разделения данных.

**Ограничение:** Разделение по структурам не устраняет автоматически запоминание опубликованных случаев языковой моделью.

## R53. Taylor et al. A randomized trial of coenzyme Q10 in confirmed statin myopathy

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/25545331/](https://pubmed.ncbi.nlm.nih.gov/25545331/)

**Дата / версия:** Онлайн 17.12.2014; Atherosclerosis 2015;238:329–335; DOI 10.1016/j.atherosclerosis.2014.12.016.

**Тип источника:** Рандомизированное исследование.

**Что подтверждает:** В этом исследовании не обнаружено уменьшения мышечной боли.

**Ограничение:** Не самостоятельное основание для полной актуальной клинической рекомендации.

## R54. Coenzyme Q10 supplementation decreases statin-related mild-to-moderate muscle symptoms

**Ссылка:** [https://pubmed.ncbi.nlm.nih.gov/25375075/](https://pubmed.ncbi.nlm.nih.gov/25375075/)

**Дата / версия:** 2014.

**Тип источника:** Рандомизированное исследование.

**Что подтверждает:** Исследование с положительным результатом в другой группе и другом дизайне.

**Ограничение:** Используется вместе с отрицательным исследованием как иллюстрация неоднородности, не как рекомендация лечения.

