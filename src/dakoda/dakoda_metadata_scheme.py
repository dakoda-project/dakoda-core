from __future__ import annotations

import io
from dataclasses import dataclass, field, fields, is_dataclass
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union, Any, Generator, Tuple

import polars as pl
from importlib_resources import files
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.models.datatype import XmlDate, XmlPeriod

# TODO: move here
from dakoda.dakoda_types import T_META
from dakoda.util import enum_from_file


# To prevent extremely long enums in code, enum values have been moved to resources
_type_mappings_dir = files('dakoda.res.type_mappings')


@enum_from_file(_type_mappings_dir.joinpath('LanguageCode.csv'))
class LanguageCode(Enum):
    """Three letter language codes.

    Attributes are Uppercased, values lowercased.

    Examples:
        >>> from dakoda.languages import LanguageCode
        >>> LanguageCode.DEU.value == 'deu'
        True
        >>> CountryType.DEU == 'DEU'
        False
        >>> CountryType.DEU == CountryType('deu')
        True
    """
    pass


@enum_from_file(_type_mappings_dir.joinpath('LanguageGroup.csv'))
class LanguageGroup(Enum):
    pass


@enum_from_file(_type_mappings_dir.joinpath('LanguageNameDe.csv'))
class LanguageNameDe(Enum):
    pass


@enum_from_file(_type_mappings_dir.joinpath('LanguageNameEn.csv'))
class LanguageNameEn(Enum):
    pass


@enum_from_file(_type_mappings_dir.joinpath('CountryType.csv'))
class CountryType(Enum):
    """
    Three-letter country codes defined in ISO 3166-1.
    Attributes are Uppercased.

    Examples:
        >>> from dakoda.countries import CountryType
        >>> CountryType.DEU.value == 'DEU'
        True
        >>> CountryType.DEU == CountryType('DEU')
        True
        >>> CountryType.DEU == 'deu'
        False
    """
    pass

@enum_from_file(_type_mappings_dir.joinpath('CountryTypeOrNa.csv'))
class CountryTypeOrNa(Enum):
    """
    A country specified as COUNTRY_TYPE or a string indicating that no value is
    available.
    """
    pass

@enum_from_file(_type_mappings_dir.joinpath('DkdTrgLang.csv'))
class DkdTrgLang(Enum):
    pass


class CoarseCefrLevel(Enum):
    """A list of coarse CEFR LEVELS .

    The A1 and A2 are merged. The same goes for the B and C levels.
    """
    A = "A"
    B = "B"
    C = "C"
    NOT_AVAILABLE = "notAvailable"


class CorpusAvailabilityType(Enum):
    """
    A list of license types by which a corpus may be available, if at all.

    :cvar CLOSED: access only for members of the DAKODA Project
    :cvar RESTRICTED: access restricted to members of German academic
        institutions
    :cvar SPECIAL_RESTRICTIONS: special restrictions
    :cvar OPEN: open; all CC-licenses
    :cvar NOT_AVAILABLE: information is not available
    """
    CLOSED = "closed"
    RESTRICTED = "restricted"
    SPECIAL_RESTRICTIONS = "special restrictions"
    OPEN = "open"
    NOT_AVAILABLE = "notAvailable"


class CorpusGroup(Enum):
    CDLK = "CDLK"
    KIEZ_DEUTSCH_KORPUS = "KiezDeutsch-Korpus"
    DISKO = "DISKO"
    EURAC_KORPORA = "EURAC-Korpora"
    FALKO = "Falko"
    FD_LEX = "FD-Lex"
    HA_MA_TA_C = "HaMaTaC"
    HA_MO_TI_C = "HaMoTiC"
    NOT_APPLICABLE = "notApplicable"


class DakodaProjectDuration(Enum):
    VALUE_2022_2025 = "2022-2025"


class DataProductionSetting(Enum):
    """
    :cvar EDUCATIONAL_SETTING:
    :cvar NATURALISTIC:
    :cvar OFFICIAL_LANGUAGE_TEST: Official language testing refers to a
        situation where language testing is performed by an approved
        language assessment body.
    :cvar RESEARCH_PROJECT:
    :cvar LANGUAGE_COURSE:
    :cvar NOT_AVAILABLE:
    """

    EDUCATIONAL_SETTING = "educational setting"
    NATURALISTIC = "naturalistic"
    OFFICIAL_LANGUAGE_TEST = "officialLanguageTest"
    RESEARCH_PROJECT = "research project"
    LANGUAGE_COURSE = "language course"
    NOT_AVAILABLE = "notAvailable"


class DataProductionSettingConceptualMode(Enum):
    """
    A list of possible ceonceptual modes in which the corpus data was produced.
    """

    SPOKEN = "spoken"
    WRITTEN = "written"
    NOT_AVAILABLE = "notAvailable"


class DataProductionSettingMode(Enum):
    """
    A list of possible modes in which the corpus data was produced.
    """

    SPOKEN = "spoken"
    WRITTEN = "written"
    NOT_AVAILABLE = "notAvailable"


class DkdContributor(Enum):
    """
    A person working for the Dakoda project.
    """

    JAMILA_BL_SING = "Jamila Bläsing"
    LUISE_B_TTCHER = "Luise Böttcher"
    SHANNY_DRUKER = "Shanny Druker"
    LISA_LENORT = "Lisa Lenort"
    ANNETTE_PORTMANN = "Annette Portmann"
    CHRISTINE_RENKER = "Christine Renker"
    JOSEF_RUPPENHOFER = "Josef Ruppenhofer"
    MATTHIAS_SCHWENDEMANN = "Matthias Schwendemann"
    IULIA_SUCUTARDEAN = "Iulia Sucutardean"
    KATRIN_WISNIEWSKI = "Katrin Wisniewski"
    TORSTEN_ZESCH = "Torsten Zesch"


class DkdInstitution(Enum):
    UNIVERSIT_T_LEIPZIG = "Universität Leipzig"
    FERN_UNIVERSIT_T_IN_HAGEN = "FernUniversität in Hagen"


class DkdProjectHead(Enum):
    """
    A principal investigator of the Dakoda project.
    """

    KATRIN_WISNIEWSKI = "Katrin Wisniewski"
    TORSTEN_ZESCH = "Torsten Zesch"


class DkdProjectName(Enum):
    """
    Vollständiger Name des DAKODA-Projekts.
    """

    DATENKOMPETENZEN_IN_DA_F_DA_Z_EXPLORATION_SPRACHTECHNOLOGISCHER_ANS_TZE_ZUR_ANALYSE_VON_L2_ERWERBSSTUFEN_IN_LERNERKORPORA_DES_DEUTSCHEN = "Datenkompetenzen in DaF/DaZ: Exploration sprachtechnologischer Ansätze zur Analyse von L2-Erwerbsstufen in Lernerkorpora des Deutschen"


class DkdProjectType(Enum):
    """
    The type of funding that supported the DADKOA project.
    """

    BUNDESMINISTERIUM_F_R_BILDUNG_UND_FORSCHUNG_BMBF = (
        "Bundesministerium für Bildung und Forschung (BMBF)"
    )


class EducationalStage(Enum):
    """
    The education stage the learner is in at the time of data collection.
    """

    EARLY_CHILDHOOD = "early childhood"
    PRIMARY = "primary"
    LOWER_SECONDARY = "lower secondary"
    UPPER_SECONDARY = "upper secondary"
    POST_SECONDARY_NON_TERTIARY = "post-secondary non-tertiary"
    SHORT_CYCLE_TERTIARY = "short-cycle tertiary"
    BACHELOR = "Bachelor"
    MASTER = "Master"
    DOCTORATE = "Doctorate"
    NOT_AVAILABLE = "notAvailable"


class FormalityType(Enum):
    """
    Formality level of the task.
    """

    INFORMAL = "informal"
    UNMARKED_TO_INFORMAL = "unmarked to informal"
    UNMARKED = "unmarked"
    UNMARKED_TO_FORMAL = "unmarked to formal"
    FORMAL = "formal"
    NOT_AVAILABLE = "notAvailable"


class Gender(Enum):
    FEMALE = "female"
    MALE = "male"
    NON_BINARY = "non-binary"
    NOT_AVAILABLE = "notAvailable"


class InteractionTypes(Enum):
    """
    A specification of the language combinations used .

    :cvar ONLY_L1_SPEAKERS: Only L1 speakers take part in the
        interaction.
    :cvar ONLY_L2_SPEAKERS: Only L2 speakers are part of the
        interaction.
    :cvar L1_AND_L2_SPEAKERS_MIXED: A mix of L1- and L2-speakers is part
        of the interaction.
    :cvar NOT_AVAILABLE:
    :cvar NOT_APPLICABLE:
    """

    ONLY_L1_SPEAKERS = "only L1-speakers"
    ONLY_L2_SPEAKERS = "only L2 speakers"
    L1_AND_L2_SPEAKERS_MIXED = "L1 and L2 speakers mixed"
    NOT_AVAILABLE = "notAvailable"
    NOT_APPLICABLE = "notApplicable"


class L1Constellation(Enum):
    MONO = "mono"
    MULTI = "multi"


class LangStatus(Enum):
    L1 = "L1"
    L2 = "L2"
    TARGET_LANGUAGE = "Target language"
    NOT_AVAILABLE = "notAvailable"


class LearnerAgeRange(Enum):
    """
    A predefined set of age ranges that are associated with different types of
    language acquisition processes.
    """

    VALUE_0_BIS_3_ERSTSPRACHERWERB = "0 bis 3, Erstspracherwerb"
    VALUE_4_BIS_6_FR_HER_KINDLICHER_ZWEITSPRACHERWERB = (
        "4 bis 6, Früher (kindlicher) Zweitspracherwerb"
    )
    VALUE_7_BIS_8_SP_TER_KINDLICHER_ZWEITSPRACHERWERB_FREMDSPRACHERWERB = (
        "7 bis 8,(Später kindlicher) Zweitspracherwerb / Fremdspracherwerb"
    )
    VALUE_9_BIS_12_SP_TER_KINDLICHER_ZWEITSPRACHERWERB_FREMDSPRACHERWERB = (
        "9 bis 12, (später kindlicher) Zweitspracherwerb / Fremdspracherwerb"
    )
    VALUE_12_BIS_18_ZWEITSPRACHERWERB_FREMDSPRACHERWERB_VON_JUGENDLICHEN_UND_ERWACHSENEN = "12 bis 18, Zweitspracherwerb / Fremdspracherwerb (von Jugendlichen und Erwachsenen)"
    VALUE_19_BIS_35_ZWEITSPRACHERWERB_FREMDSPRACHERWERB_VON_JUGENDLICHEN_UND_ERWACHSENEN = "19 bis 35, Zweitspracherwerb / Fremdspracherwerb (von Jugendlichen und Erwachsenen)"
    LTER_ALS_35_ZWEITSPRACHERWERB_FREMDSPRACHERWERB_VON_JUGENDLICHEN_UND_ERWACHSENEN = "älter als 35, Zweitspracherwerb / Fremdspracherwerb (von Jugendlichen und Erwachsenen)"
    UNKLAR_BZW_SONSTIGE = "unklar bzw. sonstige"
    NOT_AVAILABLE = "notAvailable"


class LearnerTaskType(Enum):
    """
    Type of task used in collecting the data.
    """

    BOOK_REVIEW = "book review"
    CONSULTATION = "consultation"
    CONVERSATION = "conversation"
    DESCRIPTION = "description"
    ESSAY = "essay"
    INSTRUCTION = "instruction"
    INTERVIEW = "interview"
    LETTER = "letter"
    MAP_TASK = "map task"
    NARROW_ELICITATION_TASK = "narrow elicitation task"
    POST_IN_A_FORUM = "post in a forum"
    PROBLEM_SOVLING = "problem sovling"
    REPORT = "report"
    STORY = "story"
    SUMMARY = "summary"
    TRANSLATION = "translation"
    NOT_AVAILABLE = "notAvailable"


class NaString(Enum):
    """
    A string indicating that no value is available for a metadatum or that the
    metadatum is not applicable.
    """

    NOT_AVAILABLE = "notAvailable"
    NOT_APPLICABLE = "notApplicable"


class PossibilitiesForComparisons(Enum):
    """
    Possibilities for comparing tasks and time points.

    :cvar A_1: one task, done once
    :cvar A_N: one task, done repeatedly
    :cvar M_A_N: several tasks, each done repeatedly
    :cvar M_A_1: several tasks , each done once
    :cvar NOT_AVAILABLE:
    """

    A_1 = "A-1"
    A_N = "A-n"
    M_A_N = "mA-n"
    M_A_1 = "mA-1"
    NOT_AVAILABLE = "notAvailable"


class ProficiencyAssessmentMethod(Enum):
    """
    A type of proficiency assessment.
    """

    INDEPENDENT_INSTRUMENT = "independent instrument"
    TOTAL_TEST_SCORE = "total test score"
    OTHER = "other"
    NOT_AVAILABLE = "notAvailable"


class ProficiencyAssignmentMethod(Enum):
    LEARNER_CENTRED = "learner-centred"
    TEXT_CENTRED = "text-centred"
    AUTOMATIC = "automatic"
    NONE = "none"
    NOT_AVAILABLE = "notAvailable"
    NOT_APPLICABLE = "notApplicable"


class ProficiencyAssignmentMethodType(Enum):
    """
    Method used for proficiency assessment.
    """

    SCORE_ON_TEXT = "score on text"
    TEACHER_S_EVALUATION = "teacher's evaluation"
    POST_HOC_ASSIGNMENT = "post-hoc assignment"
    NOT_AVAILABLE = "notAvailable"


class ProficiencyLevel(Enum):
    """A list of possible coarse proficiency levels specified as CEFR levels or
    ranges.

    Including value "notAvailable"
    """

    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"
    NOT_AVAILABLE = "notAvailable"


class RhetoricalFunctions(Enum):
    APPLYING = "applying"
    ARGUING = "arguing"
    ASKING_FOR_HELP = "asking for help"
    ASKING_FOR_INFORMATION = "asking for information"
    BUILD_A_SENTENCE = "build a sentence"
    COMPARING = "comparing"
    COMPLAINING = "complaining"
    DESCRIBING = "describing"
    EXPRESS_CONGRATULATIONS = "express congratulations"
    GIVING_ADVICE = "giving advice"
    INFORMING = "informing"
    INSTRUCTING = "instructing"
    NARRATING = "narrating"
    OFFERING_SOMETHING = "offering something"
    ORGANISE_MEETING = "organise meeting"
    QUESTION_AND_ANSWER = "question and answer"
    READING_ALOUD = "reading aloud"
    REPORTING = "reporting"
    SUMMARISING = "summarising"
    TRANSLATING = "translating"
    NOT_AVAILABLE = "notAvailable"


class StorageUnit(Enum):
    KB = "KB"
    MB = "MB"
    GB = "GB"
    TB = "TB"
    PB = "PB"


class StudyDesign(Enum):
    """
    The study design under which the corpus data was produced.
    """

    LONGITUDINAL = "longitudinal"
    PSEUDO_LONGITUDINAL = "pseudo-longitudinal"
    CROSS_SECTIONAL = "cross-sectional"


class TaskStimulusType(Enum):
    """
    Type of stimulus for the task.
    """

    ADVERTISEMENT = "advertisement"
    ARTICLE = "article"
    ARTICLES = "articles"
    BOOK = "book"
    COMIC = "comic"
    DESCRIPTION_OF_A_SITUATION = "description of a situation"
    DIAGRAM = "diagram"
    ESSAY = "essay"
    EXTRACT_FROM_A_DOCTORAL_DISSERTATION = "extract from a doctoral dissertation"
    EXTRACT_FROM_A_DOCTORAL_ARTICLES = "extract from a doctoral articles"
    FIGURE = "figure"
    TEXT_EDITED_FOR_TEACHING = "text edited for teaching"
    FORM = "form"
    INTERVIEW = "interview"
    JOB_ADVERTISEMENT = "job advertisement"
    LETTER = "letter"
    LIST_OF_WORDS_OR_EXPRESSIONS = "list of words or expressions"
    MAP = "map"
    ORAL_INSTRUCTIONS = "oral instructions"
    PICTURE_S = "picture(s)"
    QUESTIONNAIRE = "questionnaire"
    QUOTE = "quote"
    SCENE_ACTED_OUT = "scene acted out"
    TALKS = "talks"
    VIDEO = "video"
    WRITTEN_INSTRUCTION = "written instruction"
    NOT_AVAILABLE = "notAvailable"
    NOT_APPLICABLE = "notApplicable"


class TopicType(Enum):
    """
    A list of topic types that may be assigned to texts.
    """

    DOMESTIC = "domestic"
    DAILY_ACTIVITIES = "daily activities"
    BUSINESS_WORK_PLACE = "business/work place"
    SCIENCE = "science"
    EDUCATION_ACADEMIC = "education / academic"
    GOVERNMENT_LEGAL_POLITICS = "government / legal / politics"
    RELIGION = "religion"
    SPORTS = "sports"
    ART_ENTERTAINEMENT = "art / entertainement"
    OTHER = "other"
    NOT_AVAILABLE = "notAvailable"


class TrgLangInputType(Enum):
    """
    Dominant word order type according to WALS.
    """

    MAINLY_WITHOUT_CONTROLLED_TEACHING_PROCESSES = (
        "mainly without controlled teaching processes"
    )
    MAINLY_IN_CONTROLLED_TEACHING_CONTEXTS = "mainly in controlled teaching contexts"
    HYBRID = "hybrid"
    NOT_AVAILABLE = "notAvailable"


class WordOrderType(Enum):
    """
    Dominant word order type according to WALS.
    """

    SOV = "SOV"
    SVO = "SVO"
    VSO = "VSO"
    SVO_VSO = "SVO ; VSO"
    SOV_SVO = "SOV; SVO"
    NO_DOMINANT_ORDER = "no dominant order"
    UNCLEAR = "unclear"
    NOT_AVAILABLE = "notAvailable"


@dataclass
class Annotation:
    """
    :ivar annotation_automatic: Was the annotation process fully
        automatic? An equivalent field in LC-meta is
        `annotation_automatic`.
    :ivar annotation_corrected: Was the automatic annotation subject to
        further correction?  An equivalent field in LC-meta is
        `annotation_corrected`.
    :ivar annotation_documentation: Plain text description of annotation
        or link to documentation An equivalent field in LC-meta is
        `annotation_documentation`.
    :ivar annotation_evaluation: Was the annotation evaluated? An
        equivalent field in LC-meta is `annotation_evaluation`.
    :ivar annotation_tool: Name of tool used for annotation An
        equivalent field in LC-meta is `annotation_tool`.
    :ivar annotation_toolVersion: Version of tool used for annotation An
        equivalent field in LC-meta is `annotation_tool_version`.
    :ivar annotation_modelVersion: Version of a trained statistical
        model or parameter set for use with the annotation tool. LC-meta
        has no related field.
    :ivar annotation_type: Specification of an annotation type(s) such
        as lemma , POS, etc. that are provided by the tool in question.
        An equivalent field in LC-meta is `annotation_type`.
    """

    annotation_automatic: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    annotation_corrected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    annotation_documentation: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    annotation_evaluation: Optional[Union[bool, NaString]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    annotation_tool: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    annotation_toolVersion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    annotation_modelVersion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    annotation_type: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class CorpusAdministrative:
    """
    :ivar corpus_admin_acronym: Corpus acronym. An equivalent field in
        LC-meta is `corpus_acronym`.
    :ivar corpus_admin_name: The fully disabbreviated title of the
        corpus. Can occur multiple times for corpora with official names
        in multiple languages. An equivalent field in LC-meta is
        `corpus_name`.
    :ivar corpus_admin_author: Corpus creator. An equivalent field in
        LC-meta is  `corpus_author`.
    :ivar corpus_admin_availability: Licensing terms and conditions for
        corpus. An equivalent field in LC-meta is `corpus_availability`
    :ivar corpus_admin_citationDocument: Information on how excerpts of
        the corpus should be referenced. This field has no counterpart
        in LC-meta .
    :ivar corpus_admin_citeAs: Corpus citation. An equivalent field in
        LC-meta is `corpus_cite_as`.
    :ivar corpus_admin_contactMail: Contact e-mail address . An
        equivalent field in LC-meta is `corpus_contact_mail`.
    :ivar corpus_admin_contributor_dkd: Contributor (DAKODA version).
        LC-meta has the comparable field `corpus_contributor`.
    :ivar corpus_admin_contributor_orig: Contributor (original version).
        LC-meta has the comparable field `corpus_contributor`.
    :ivar corpus_admin_dateOfPublication: Publication year of the source
        version of the corpus. An comparable field name in LC-meta is
        `corpus_date_of_publication`.
    :ivar corpus_admin_documentation:
    :ivar corpus_admin_fileFormat: File format (DAKODA-Version). An
        equivalent field in LC-meta is `corpus_file_format`.
    :ivar corpus_admin_licence: Licence name (DAKODA version).  An
        equivalent field in LC-meta is `corpus_licence`.
    :ivar corpus_admin_licenceFulltext: Licence text (DAKODA version).
        There is no equivalent field in LC-meta.
    :ivar corpus_admin_licenceUrl: Link to licence text. An equivalent
        field in LC-meta is `corpus_licence_url`.
    :ivar corpus_admin_otherVersions: Associated version of the corpus.
        This will often be an earlier release of the corpus. An
        equivalent field in LC-meta is `corpus_other_versions`.
    :ivar corpus_admin_pid_dkd: Persistent identifier (DAKODA version).
        An equivalent field in LC-meta is `corpus_pid`. <xs:appinfo
        xmlns:xs="http://www.w3.org/2001/XMLSchema"><displayname
        xmlns="">PID (DAKODA-Version)</displayname></xs:appinfo>
    :ivar corpus_admin_pid_orig: Persistent Identifier (original
        version). An equivalent field in LC-meta is  `corpus_pid`.
    :ivar corpus_admin_refArticle: Reference article. Such articles
        typically contain an extensive verbal description of the corpus
        and its design. An equivalent field in LC-meta is
        `corpus_ref_article`.
    :ivar corpus_admin_referencesOther: Further important publications
        or links to the corpus . LC-meta has related metadata field
        `corpus_ref_article`.
    :ivar corpus_admin_researchPaper: Further publications (original
        version). An equivalent field in LC-meta is
        corpus_ref_article`.
    :ivar corpus_admin_URL_download: Link to corpus download (original
        version). There is no equivalent field in LC-meta.
    :ivar corpus_admin_URLquery: Link to corpus query (original
        version).
    :ivar corpus_admin_version_orig: Data version on which the DAKODA
        version is based: Version number, PID or download link with
        date. An equivalent field in LC-meta is `corpus_version`.
    """

    corpus_admin_acronym: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    corpus_admin_name: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    corpus_admin_author: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    corpus_admin_availability: Optional[CorpusAvailabilityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_admin_citationDocument: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_admin_citeAs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
        },
    )
    corpus_admin_contactMail: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "pattern": r"([^@]+@[^\.]+\..+)|(notAvailable)",
        },
    )
    corpus_admin_contributor_dkd: List[DkdContributor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 11,
            "max_occurs": 11,
        },
    )
    corpus_admin_contributor_orig: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    corpus_admin_dateOfPublication: Optional[
        Union[XmlPeriod, XmlDate, str, NaString]
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"\d{4}-\d{2}",
        },
    )
    corpus_admin_documentation: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    corpus_admin_fileFormat: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    corpus_admin_licence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_admin_licenceFulltext: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    corpus_admin_licenceUrl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_admin_otherVersions: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    corpus_admin_pid_dkd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_admin_pid_orig: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_admin_refArticle: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    corpus_admin_referencesOther: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    corpus_admin_researchPaper: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    corpus_admin_URL_download: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    corpus_admin_URLquery: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    corpus_admin_version_orig: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CorpusDesign:
    """
    :ivar corpus_design_description: A short description of the corpus.
        An equivalent field in LC-meta is `corpus_description` in LC-
        meta.
    :ivar corpus_design_designType: Design of data collection/study
        design. An equivalent field in LC-meta `corpus_longitudinal`.
    :ivar corpus_design_group: Affiliation of the corpus to a corpus
        group. An equivalent field in LC-meta is `corpus_related`.
    :ivar corpus_design_isComparableDataIncluded: Does the corpus
        include comparison data? An equivalent field in LC-meta is
        `corpus_comparable_data_included`.
    :ivar corpus_design_l1Language: L1 language(s). An equivalent field
        in LC-meta is `corpus_L1_language`.
    :ivar corpus_design_l1Type: L1 constellation. If all participants
        share one L1: mono; if there are multiple L1s: multi . There is
        no eqivalent field in LC-meta.
    :ivar corpus_design_size: Storage requirement in KB, MB, GB, TB or
        PB. An equivalent field in LC-meta is  `corpus_size`.
    :ivar corpus_design_targetLanguage: Target languages of the complete
        corpus. An equivalent field in LC-meta is
        `corpus_target_language`.
    :ivar corpus_design_targetLanguageType: Target languages of the
        complete corpus. If only German is the target language, this is
        coded as mono. When there are other target languages in addition
        to German , this is coded as multi.
    :ivar corpus_design_timeOfDataCollection: The year or span of years
        during which the corpus was created. An equivalent field in LC-
        meta is `corpus_time_of_data_collection`.
    """

    class Meta:
        name = "Corpus_Design"

    corpus_design_description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
        },
    )
    corpus_design_designType: Optional[StudyDesign] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_design_group: Optional[CorpusGroup] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    corpus_design_isComparableDataIncluded: Optional[Union[bool, NaString]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_design_l1Language: List[LanguageNameDe] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    corpus_design_l1Type: List[L1Constellation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    corpus_design_size: Optional["CorpusDesign.CorpusDesignSize"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_design_targetLanguage: List[DkdTrgLang] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    corpus_design_targetLanguageType: List[L1Constellation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    corpus_design_timeOfDataCollection: Optional[
        Union[XmlPeriod, str, NaString]
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"\d{4}-\d{4}",
        },
    )

    @dataclass
    class CorpusDesignSize:
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        unit: Optional[StorageUnit] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class CorpusProficiency:
    """
    :ivar corpus_proficiency_assignmentMethod: The method of proficiency
        level assignment used for the corpus . An equivalent field in
        LC-meta is `corpus_proficiency_assignment_method`.
    :ivar corpus_proficiency_isAssignmentAvailable: specification of
        whether the corpus contains proficiency scores for individual
        learner/L1 speakers or texts. A related field in LC-meta is
        `corpus_proficiency_assignment_available`.
    :ivar corpus_proficiency_learner_AssignmentInstrument: Name of test
        instrument used to evaluate learners’ proficiency. CMSCL has
        matching field
        `corpus_learner_proficiency_assignment_instrument`.
    :ivar corpus_proficiency_levelMax: proficiency levels; if only
        approximately known, enter the maximum value here. A related
        field in LC-meta is `corpus_proficiency_level`.
    :ivar corpus_proficiency_levelMin: proficiency levels; if only
        approximately known, enter the minimum value here. An equivalent
        field in LC-meta is `corpus_proficiency_level`.
    :ivar corpus_proficiency_textAssignmentInstrument: Name of
        instrument used to evaluate texts’ proficiency. A related field
        in LC-meta is `corpus_text_proficiency_assignment_instrument`.
    :ivar corpus_proficiency_textAutomaticAssignmentInstrument:
        Specification of the automatic instrument used to assess the
        profiency of a text. A related field in LC-meta is
        `corpus_text_proficiency_assignment_instrument`.
    """

    class Meta:
        name = "Corpus_Proficiency"

    corpus_proficiency_assignmentMethod: ProficiencyAssignmentMethod = field(
        default=ProficiencyAssignmentMethod.NONE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_proficiency_isAssignmentAvailable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_proficiency_learner_AssignmentInstrument: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    corpus_proficiency_levelMax: Optional[ProficiencyLevel] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_proficiency_levelMin: Optional[ProficiencyLevel] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_proficiency_textAssignmentInstrument: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_proficiency_textAutomaticAssignmentInstrument: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CorpusProject:
    """
    :ivar corpus_project_contact_orig: Contact e-mail address of the
        source project (original version). LC-meta has a matching field
        `corpus_contact_mail`.
    :ivar corpus_project_duration_dkd: Duration of the project (DAKODA)
    :ivar corpus_project_duration_orig: Duration of the project
        (original version)
    :ivar corpus_project_head_dkd: One of the PIs of the Dakoda project.
    :ivar corpus_project_head_orig: Head(s) of the creation project
        (original version).
    :ivar corpus_project_institution_dkd: One of the institutions
        responsible for creating the DAKODA version of the corpus. A
        comparable field in LC-meta is `corpus_publisher`. <xs:appinfo
        xmlns:xs="http://www.w3.org/2001/XMLSchema"><displayname
        xmlns="">Einrichtungen von DAKODA</displayname></xs:appinfo>
    :ivar corpus_project_institution_orig: Institutions responsible for
        creating the source version of the corpus. If corpus resulted
        from Phd or other thesis, the relevant institution is the
        degree-conferring one. A comparable field in LC-meta is
        `corpus_publisher`.
    :ivar corpus_project_name_dkd: Name of the project (DAKODA version)
    :ivar corpus_project_name_orig: Name of related research project.
    :ivar corpus_project_type_dkd: Type of project (DAKODA)
    :ivar corpus_project_type_orig: Type of project: Funding type and
        project number of the funding organisation (original version)
    :ivar corpus_project_URL_dkd: Link to related research project. A
        related variable in LC-meta is
        `corpus_related_research_project_URL`
    :ivar corpus_project_URL_orig: Link to related research project. A
        related variable in LC-meta is
        `corpus_related_research_project_URL`
    """

    class Meta:
        name = "Corpus_Project"

    corpus_project_contact_orig: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "pattern": r"([^@]+@[^\.]+\..+)|(notAvailable)",
        },
    )
    corpus_project_duration_dkd: Optional[DakodaProjectDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_project_duration_orig: Optional[Union[XmlPeriod, str, NaString]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"\d{4}-\d{4}",
        },
    )
    corpus_project_head_dkd: List[DkdProjectHead] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    corpus_project_head_orig: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    corpus_project_institution_dkd: List[DkdInstitution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    corpus_project_institution_orig: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    corpus_project_name_dkd: Optional[DkdProjectName] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_project_name_orig: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    corpus_project_type_dkd: DkdProjectType = field(
        init=False,
        default=DkdProjectType.BUNDESMINISTERIUM_F_R_BILDUNG_UND_FORSCHUNG_BMBF,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_project_type_orig: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_project_URL_dkd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    corpus_project_URL_orig: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CorpusSubcorpus:
    """
    :ivar corpus_subcorpus_signet: Identifier of the (sub)corpus in the
        DAKODA repository.
    :ivar corpus_subcorpus_sizeLearners: The number of learners
        represented in the subcorpus. An equivalent field in LC-meta is
        `corpus_size_learners`.
    :ivar corpus_subcorpus_sizeTexts: The number of texts in the
        subcorpus. A related field in LC-meta is `corpus_size_texts`.
    :ivar corpus_subcorpus_sizeTokens: The number of tokens in the
        subcorpus. A related field in LC-meta is `corpus_size_tokens`.
    :ivar corpus_subcorpus_targetLanguage: Specification of the target
        language in a subcorpus as a value followig ISO 639-3. A related
        field in LC-meta is `corpus_target_language`.
    """

    class Meta:
        name = "Corpus_Subcorpus"

    corpus_subcorpus_signet: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_subcorpus_sizeLearners: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_subcorpus_sizeTexts: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_subcorpus_sizeTokens: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_subcorpus_targetLanguage: List[DkdTrgLang] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class InteractionBlock:
    """
    :ivar task_interaction_conceptualMode: Conceptual orality
        (immediacy) or conceptual literacy (distance) according to Koch
        and Oesterreicher's model of "Nähe und Distanz" . An equivalent
        field in LC-meta is `situation_medium`.
    :ivar task_interaction_ExpectedRhetoricalFunctions: The
        communicative purpose. An equivalent field in LC-meta is
        `XXX`.`situation_purpose`.
    :ivar task_interaction_formality: Formality level of the task.
        Related fields in LC-meta are  `situation_mode` and
        `corpus_mode`.
    :ivar task_interaction_mode: Corpus modality. Related fields in LC-
        meta are `corpus_mode` and `situation_mode`.
    :ivar task_interaction_participantsL1L2Interaction: Type of
        interaction. There is no related field in LC-meta.
    :ivar task_interaction_participants: Number of speakers. An
        equivalent field in LC-meta is `corpus_single_or_multi_author`.
    :ivar task_interaction_type: Register. An equivalent field in LC-
        meta is `situation_register`.
    """

    class Meta:
        name = "Interaction_Block"

    task_interaction_conceptualMode: List[DataProductionSettingConceptualMode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    task_interaction_ExpectedRhetoricalFunctions: List[RhetoricalFunctions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    task_interaction_formality: FormalityType = field(
        default=FormalityType.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    task_interaction_mode: List[DataProductionSettingMode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    task_interaction_participantsL1L2Interaction: Optional[InteractionTypes] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    task_interaction_participants: List[Union[int, str, NaString]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "pattern": r"\d{1,2}-\d{1,2}",
        },
    )
    task_interaction_type: LearnerTaskType = field(
        default=LearnerTaskType.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LanguageExposure:
    """
    :ivar learner_language_exposure_onset: Age of Onset. Related field
        in CMSCL are `learner_target_language_onset` and
        `learner_L"_language_onset`.
    :ivar learner_language_exposure_onset_group: Age bracket within
        which the start of acquisition for the language in question
        falls. There is no related field in CMSCL.
    :ivar learner_language_exposure_durationOfInstruction: Number of
        years of instruction of a foreign or second language. Not
        applicable to L1-instruction. A related field in CMSCL is
        `learner_target_language_learning_context` .
    :ivar learner_language_exposure_durationOfUse: Number of years in
        which learner used German (any form of learning or contact
        time). In cases, where the language in question is an L1, this
        value can be equated to the person's age at the time of text
        producton. A related field in CMSCL is
        `learner_target_language_learning_context` .
    :ivar learner_language_exposure_input: Type of input through which
        the learner came into contact with the language. A related field
        in CMSCL is `learner_target_language_learning_context`.
    :ivar learner_language_exposure_institution: Type of institution in
        which the learner learnt the language . There is a related field
        `months_spent_target_language_environment` in CMSCL.
    :ivar learner_language_exposure_monthsSpentEnvironment: Cumulative
        time (in months) spent in an environment where the L2 is spoken.
        A related field in CMSCL are
        `learner_L2_months_spent_L2_environment` and
        `months_spent_target_language_environment` .
    :ivar learner_language_exposure_learningContext: Learning context of
        target language from onset to current age. There is no related
        field in LC-meta.
    :ivar learner_language_exposure_placeAcquisition: Place where
        learner mainly has learnt German (specified as a country or
        territory according to ISO 3166-ALPHA-3). A related field in
        CMSCL is `learner_target_language_learning_context`.
    :ivar learner_language_exposure_WasInEnvironment: Was the learner/L1
        speaker in a country/region where the target language is spoken
        at the time of data collection? A related field in CMSCL is
        `learner_target_language_environment`.
    :ivar learner_language_WasInstructed: Was the learner/L1 speaker in
        an instructed learning context at the time of data collection? A
        related field in CMSCL is `learner_target_language_instructed`.
    """

    class Meta:
        name = "Language_Exposure"

    learner_language_exposure_onset: Optional[Union[int, float, NaString]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_exclusive": 0,
        },
    )
    learner_language_exposure_onset_group: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_exposure_durationOfInstruction: Optional[
        Union[int, float, NaString]
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_exclusive": 0,
        },
    )
    learner_language_exposure_durationOfUse: Optional[
        Union[int, float, NaString]
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_exclusive": 0,
        },
    )
    learner_language_exposure_input: Optional[TrgLangInputType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_exposure_institution: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    learner_language_exposure_monthsSpentEnvironment: Optional[
        Union[int, float, NaString]
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_exclusive": 0,
        },
    )
    learner_language_exposure_learningContext: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_exposure_placeAcquisition: Optional[CountryTypeOrNa] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_exposure_WasInEnvironment: Optional[Union[bool, NaString]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_WasInstructed: Optional[Union[bool, NaString]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LearnerLanguageProficiency:
    """
    :ivar learner_language_proficiency_score: learner/L1 speaker
        proficiency (not harmonised across DAKODA corpora) A related
        field in LC-meta is `learner_target_language_proficiency`.
    :ivar learner_language_proficiency_cefrMax: Learners'  maximal level
        of language proficiency (CEFR). A related field in LC-meta is
        `learner_target_language_proficiency`.
    :ivar learner_language_proficiency_cefrMin: Learners' minimal level
        of language proficiency (CEFR). A related field in LC-meta is
        `learner_target_language_proficiency`.
    :ivar learner_language_proficiency_cTestCefrMax: Maximum level of
        CEFR-related c-tests. A related field in LC-meta is
        `learner_target_language_proficiency_CEFR_conversion`.
    :ivar learner_language_proficiency_cTestCefrMin: Minimum level of
        CEFR-related c-tests. A related field in LC-meta is
        `learner_target_language_proficiency_CEFR_conversion`.
    :ivar learner_language_proficiency_cTestLevelDetail: Detailed c-test
        level. An equivalent field in LC-meta is
        `learner_target_language_proficiency`.
    :ivar learner_language_proficiency_cTestPercent: c-test result in
        per cent. A related field in LC-meta is
        `learner_target_language_proficiency`.
    :ivar learner_language_proficiency_cTestType: Name of the c-test .
        An equivalent field in LC-meta is
        `corpus_learner_proficiency_assignment_instrument`.
    :ivar learner_language_proficiency_estimateMax: Approximate
        indication of the speaker's language competence; if possible,
        based on GeR-related text assessment; if not, based on C-test
        result or duration of use (0-2 years = A2, 2-5 years = B2, &gt;5
        years = C2. If the level cannot be specified precisely, the
        upper limit of the estimated competence is given here. A related
        field in LC-meta is `learner_target_language_proficiency`.
    :ivar learner_language_proficiency_estimateMin: Approximate
        indication of the speaker's language competence; if possible,
        based on GeR-related text assessment; if not, based on C-test
        result or duration of use (0-2 years = A2, 2-5 years = B2, &gt;5
        years = C2. If the level cannot be specified precisely, the
        lower limit of the estimated competence is given here. .A
        related field in LC-meta is
        `learner_target_language_proficiency`.
    :ivar learner_language_proficiency_selfAssessment: Self-assessment
        of language skills. An equivalent field in LC-meta is
        `learner_L2_language_proficiency`.
    :ivar learner_language_proficiency_assignmentInstrument: Name of
        instrument used to evaluate learners’ proficiency. An equivalent
        field in LC-meta is
        `corpus_learner_proficiency_assignment_instrument`.
    :ivar learner_language_proficiency_assignmentMethod: How was the
        proficiency of the learner evaluated?  An equivalent field in
        LC-meta is `corpus_learner_proficiency_assignment_method`.
    :ivar learner_language_proficiency_documentation: Link to relevant
        documentation on how learners were evaluated. An equivalent
        field in LC-meta is `corpus_learner_proficiency_documentation`.
    """

    class Meta:
        name = "Learner_Language_Proficiency"

    learner_language_proficiency_score: Optional[Union[int, Decimal, str]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_proficiency_cefrMax: Optional[ProficiencyLevel] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_proficiency_cefrMin: Optional[ProficiencyLevel] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_proficiency_cTestCefrMax: Optional[ProficiencyLevel] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_proficiency_cTestCefrMin: Optional[ProficiencyLevel] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_proficiency_cTestLevelDetail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_proficiency_cTestPercent: Optional[
        Union[Decimal, NaString]
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("100"),
        },
    )
    learner_language_proficiency_cTestType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_proficiency_estimateMax: Optional[ProficiencyLevel] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_proficiency_estimateMin: Optional[ProficiencyLevel] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_proficiency_selfAssessment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_proficiency_assignmentInstrument: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_proficiency_assignmentMethod: List[
        ProficiencyAssessmentMethod
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    learner_language_proficiency_documentation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Lingua:
    name_de: Optional[LanguageNameDe] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name_en: Optional[LanguageNameEn] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    iso_code_639_3: Optional[LanguageCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    group: Optional[LanguageGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ProductionSetting:
    """
    :ivar production_setting_schoolGrade: School year in which the
        productions were collected. There is no related field in LC-
        meta.
    :ivar productionSetting_educationalStage: Level of education the
        learners are currently in and have not yet completed. An
        equivalent field in LC-meta is `learner_educational_background`.
    :ivar productionSetting_languageTest: If the texts were collected as
        part of an official language test, this represents the full name
        of the language test taken. LC-meta has a related field
        `corpus_language_testing_setting`.
    :ivar productionSetting_languageCourseLevel: Level of the language
        course currently attended. LC-meta has no equivalent field.
    :ivar productionSetting_naturalistic: Specification of the
        elicitation context if outside institutional contexts. Possible
        values include e.g. work, family, friends, leisure. A related
        field in LC-meta is `situation_setting`.
    :ivar productionSetting_collectedInResearchProject: Was the data
        collected as part of a research project?
    :ivar productionSetting_setting: Language production setting. An
        equivalent field in LC-meta is `corpus_production_setting`.
    """

    class Meta:
        name = "Production_Setting"

    production_setting_schoolGrade: Optional[Union[int, NaString]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    productionSetting_educationalStage: List[EducationalStage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    productionSetting_languageTest: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    productionSetting_languageCourseLevel: str = field(
        default="notApplicable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    productionSetting_naturalistic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    productionSetting_collectedInResearchProject: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    productionSetting_setting: List[DataProductionSetting] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Sociodemographics:
    """
    :ivar learner_socio_birthplace: Place of birth of the speaker. This
        is coded as country or territory. There is no related field in
        CMSCL.
    :ivar learner_socio_country: Country in which the learner spent most
        of his/her childhood. There is a related field in CMSCL,
        `learner_country`.
    :ivar learner_socio_educationalBackground: Highest level of
        education attained by the learner. There is a related field in
        LC-meta called `learner_educational_background`.
    :ivar learner_socio_gender: Learner/L1 speaker gender. An equivalent
        field in LC-meta is `learner_gender`.
    :ivar learner_socio_majorSubject: (Major) subject at university.
        There is no related field in LC-meta .
    :ivar learner_socio_profession: Occupation. An equivalent field in
        LC-meta is `learner_socioeconomic_status`.
    :ivar learner_socio_schoolGrade: School year in which the text was
        collected. There is no related field in LC-meta .
    """

    learner_socio_birthplace: CountryType = field(
        default=CountryType.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_socio_country: CountryType = field(
        default=CountryType.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_socio_educationalBackground: EducationalStage = field(
        default=EducationalStage.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_socio_gender: Gender = field(
        default=Gender.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_socio_majorSubject: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    learner_socio_profession: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    learner_socio_schoolGrade: Optional[Union[int, NaString]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TargetHypothesis:
    """
    :ivar targetHypothesis_automatic: Was the th generation done fully
        automatically? A related field in LC-meta is
        `annotation_automatic`.
    :ivar targetHypothesis_corrected: Were the automatically generated
        ths subject to further correction?  A related field in LC-meta
        is `annotation_corrected`.
    :ivar targetHypothesis_documentation: Plain text description of TH
        generation process or link to documentation A related field in
        LC-meta is `annotation_documentation`.
    :ivar targetHypothesis_evaluation: Were the automatically generated
        THs evaluated? A related field in LC-meta is
        `annotation_evaluation`.
    :ivar targetHypothesis_tool: Name of tool used for generation of
        THs. A related field in LC-meta is `annotation_tool`.
    :ivar targetHypothesis_toolVersion: Version of tool used for
        generating THs. A related field in LC-meta is
        `annotation_tool_version`.
    """

    class Meta:
        name = "Target_Hypothesis"

    targetHypothesis_automatic: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    targetHypothesis_corrected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    targetHypothesis_documentation: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    targetHypothesis_evaluation: Optional[Union[bool, NaString]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    targetHypothesis_tool: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    targetHypothesis_toolVersion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TextAnnotation:
    """
    :ivar text_annotation_borrowed_orig: Does the text contain
        annotations for structures taken from the task prompt? There is
        no related field in LC-meta .
    :ivar text_annotation_hasErrorAnnotation_orig: Is the text error-
        annotated? There is no related field in LC-meta .
    :ivar text_annotation_hasTargetHypotheses: Does the text have a
        target hypothesis or other type of normalisation? There is no
        related field in LC-meta.
    """

    class Meta:
        name = "Text_Annotation"

    text_annotation_borrowed_orig: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_annotation_hasErrorAnnotation_orig: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_annotation_hasTargetHypotheses: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TextLearner:
    """
    :ivar text_learner_ageProduction: Age at time of text production. An
        equivalent field in LC-meta is `learner_age`.
    :ivar text_learner_ageProductionAggregated: Rough age range at the
        time of the data collection . A related field in LC-meta is
        `learner_age`.
    :ivar text_learner_role: Role of the person in this event . There is
        no related field in LC-meta .
    """

    class Meta:
        name = "Text_Learner"

    text_learner_ageProduction: Union[int, float, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
            "min_exclusive": 0,
        },
    )
    text_learner_ageProductionAggregated: LearnerAgeRange = field(
        default=LearnerAgeRange.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_learner_role: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class TextProficiency:
    """
    :ivar text_proficiency_assignmentInstrument: Name of instrument used
        to evaluate a text's proficiency. An equivalent field in LC-meta
        is `corpus_text_proficiency_assignment_instrument`.
    :ivar text_proficiency_assignmentMethod: How were the texts
        evaluated? An equivalent field in LC-meta is
        `corpus_text_proficiency_assignment_method .
    :ivar text_proficiency_cefrMax: Conversion of maximum text
        proficiency score to CEFR. An equivalent field in LC-meta is
        `text_proficiency_CEFR_conversion`.
    :ivar text_proficiency_cefrMin: Conversion of minimum text
        proficiency score to CEFR. An equivalent field in LC-meta is
        `text_proficiency_CEFR_conversion`.
    :ivar text_proficiency_cefrAutomMax: Automatically generated level
        based on CEFR; maximum value of the result. A related field in
        LC-meta is `text_proficiency`.
    :ivar text_proficiency_cefrAutomMin: Automatically generated level
        based on CEFR; minimum value of the result. A related field in
        LC-meta is `text_proficiency`.
    :ivar text_proficiency_documentation: Link to relevant documentation
        on how texts were evaluated (descriptors, rubric, etc.).An
        equivalent field in LC-meta is
        `corpus_text_proficiency_documentation`.
    :ivar text_proficiency_official_languageTestingScore: Results of the
        official language test (score for the text; not global score
        which should be recorded at the level of the learner/L1 speaker
        metadata). An equivalent field in LC-meta is
        `text_official_language_testing_score`.
    :ivar text_proficiency_score: Proficiency score or level for the
        text (not harmonised across DAKODA corpora). An equivalent field
        in LC-meta is `text_proficiency`.
    """

    class Meta:
        name = "Text_Proficiency"

    text_proficiency_assignmentInstrument: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_proficiency_assignmentMethod: ProficiencyAssignmentMethodType = field(
        default=ProficiencyAssignmentMethodType.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_proficiency_cefrMax: CoarseCefrLevel = field(
        default=CoarseCefrLevel.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_proficiency_cefrMin: CoarseCefrLevel = field(
        default=CoarseCefrLevel.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_proficiency_cefrAutomMax: ProficiencyLevel = field(
        default=ProficiencyLevel.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_proficiency_cefrAutomMin: ProficiencyLevel = field(
        default=ProficiencyLevel.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_proficiency_documentation: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_proficiency_official_languageTestingScore: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_proficiency_score: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Annotator:
    """
    :ivar annotator_id: Unique identifier for manual annotator A related
        field in LC-meta is `annotator_id`.
    :ivar annotator_L1: Annotator L1.  An equivalent field in LC-meta is
        `annotator_L1`.
    :ivar annotator_L2: Annotator L2.  An equivalent field in LC-meta is
        `annotator_L2`.
    :ivar annotator_note: Any comments regarding the annotator. An
        equivalent field in LC-meta is `annotator_note`.
    :ivar annotator_targetLanguageCompetence: Annotator target language
        competence . An equivalent field in LC-meta is
        `annotator_target_language_competence`.
    :ivar annotator_type: Annotator experience. An equivalent field in
        LC-meta is `annotator_type`.
    """

    annotator_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    annotator_L1: Optional[Lingua] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    annotator_L2: Optional[Lingua] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    annotator_note: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    annotator_targetLanguageCompetence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    annotator_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Corpus:
    """
    :ivar administrative: Administrative information about the corpus.
    :ivar design: Information about the corpus design.
    :ivar proficiency: Information about the corpus proficiency.
    :ivar project: Information about the project from which the corpus
        originated.
    :ivar subcorpus: Information about a subcorpus of the corpus.
    """

    administrative: Optional[CorpusAdministrative] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    design: Optional[CorpusDesign] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    proficiency: Optional[CorpusProficiency] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    project: Optional[CorpusProject] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    subcorpus: Optional[CorpusSubcorpus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LanguageOfSpeaker:
    """
    :ivar learner_language_iso639_3: Depending on the context, this
        represents information about the Learner's L1, their L2 and/or
        the target language.
    :ivar learner_language_status: What status does the language have
        for the learner? There is no single equivalent field in LC-meta.
    :ivar learner_language_IsTarget: Is there a text for the language in
        the corpus?
    :ivar learner_language_dominantWordOrder: Word order types of L2
        according to WALS
    :ivar learner_language_group: language genus according to WALS
    :ivar learner_language_isSpokenHome: Is the language(s) spoken at
        home
    :ivar learner_language_isSpokenSchool: Is the language(s) spoken in
        school
    :ivar learner_language_parentL1: Parent L1(s)
    :ivar exposure:
    :ivar proficiency:
    """

    class Meta:
        name = "Language_Of_Speaker"

    learner_language_iso639_3: Optional[Lingua] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_status: List[LangStatus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    learner_language_IsTarget: Optional[Union[bool, NaString]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_dominantWordOrder: List[WordOrderType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    learner_language_group: Optional[LanguageGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_isSpokenHome: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_language_isSpokenSchool: List[Union[bool, NaString]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    learner_language_parentL1: Optional[LanguageCode] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    exposure: Optional[LanguageExposure] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    proficiency: Optional[LearnerLanguageProficiency] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class TaskBlock:
    """
    :ivar task_id: Unique identifier for the language situation. An
        equivalent field in LC-meta is `situation_id`.
    :ivar task_id_orig: The ID of the task within the source corpus. An
        equivalent field in LC-meta is `situation_id`.
    :ivar task_title: The title of the task. There is no related field
        in LC-meta.
    :ivar task_comparison: Possibility of comparing tasks and time
        points. There is no related field in LC-meta .
    :ivar task_description: Short description of the task. A related
        field in LC-meta is  `task_instructions`.
    :ivar task_descriptionDetailed: Further descriptions with source
        reference. A related field in LC-meta is `task_instructions`.
    :ivar task_durationMinutes: Task duration in minutes.  An equivalent
        field in LC-meta is `task_duration_minutes`.
    :ivar task_instructions: Wording of the task. A related field in LC-
        meta is `task_instructions`.
    :ivar task_isDurationLimited: Was the task timed or not? A related
        field in LC-meta is `task_duration`.
    :ivar task_levelMax: CEFR level of the task;  if only approximately
        known, enter the maximum value here. There is no related field
        in LC-meta .
    :ivar task_levelMin: CEFR level of the task; if only approximately
        known, enter the minimum value here. There is no related field
        in LC-meta .
    :ivar task_assessed: Was the task part of an exam or any other type
        of language assessment settings (informal or for obtaining a
        certificate)? A related field in LC-meta is `task_assessed`.
    :ivar task_officialLanguageTest: Is the task taken as part of an
        official assignment? A related field in LC-meta is
        `task_assessed`.
    :ivar task_officialLanguageTestSpecific: Official language test from
        which the task originates. There is no related field in LC-meta
        .
    :ivar task_options: Were learners able to choose between different
        tasks? There is no related field in LC-meta .
    :ivar task_stimulusOffered: Does the task include material as a
        stimulus for solving the task (e.g. diagram, article, etc.)?
        There is no related field in LC-meta .
    :ivar task_stimulusType: Categorisation of the stimulus material.
        There is no related field in LC-meta .
    :ivar interaction:
    """

    class Meta:
        name = "Task_Block"

    task_id: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    task_id_orig: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    task_title: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    task_comparison: List[PossibilitiesForComparisons] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    task_description: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    task_descriptionDetailed: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    task_durationMinutes: Union[int, str, NaString] = field(
        default=NaString.NOT_APPLICABLE,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"\d{1,3}-\d{1,3}",
        },
    )
    task_instructions: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    task_isDurationLimited: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    task_levelMax: List[ProficiencyLevel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    task_levelMin: List[ProficiencyLevel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    task_assessed: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    task_officialLanguageTest: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    task_officialLanguageTestSpecific: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    task_options: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    task_stimulusOffered: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    task_stimulusType: List[TaskStimulusType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    interaction: Optional[InteractionBlock] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TextProperties:
    """
    :ivar text_file: Shared ID for files related to the same learner
        production (copies of handwritten texts in pdf, transcriptions,
        sound files, videos, etc.).  An equivalent field in LC-meta is
        `text_file.
    :ivar text_id: Unique identifier for the text. A related field in
        LC-meta is `text_id`.
    :ivar text_ID_orig: Unique identifier(s) for the text (original
        version). A related field in LC-meta is `text_id`.
    :ivar text_language: Language. An eqivalent field in LC-meta is
        `text_language`.
    :ivar text_longitudinalOrder: Number that reflects a particular
        iteration in case the text was collected as part of a sequence
        of longitudinally collected data. There is no related field in
        LC-meta .
    :ivar text_timeOfCreation: Time of creation. An equivalent field in
        LC-meta is `text_time_of_creation`.
    :ivar text_tokenCount: Number of tokens in the text. An equivalent
        field in LC-meta is `text_token_count`.
    :ivar text_clauseCount: Number of sentences. There is no related
        field in LC-meta .
    :ivar text_topicAutom: Automatically assigned topic of the text . An
        equivalent field in LC-meta is `situation_topic_domain`.
    :ivar text_note: Any comments on the text and its origins. An
        equivalent field in LC-meta is `text_note`.
    :ivar learner:
    :ivar proficiency:
    :ivar annotation:
    """

    class Meta:
        name = "Text_Properties"

    text_file: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_ID_orig: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_language: Optional[Lingua] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_longitudinalOrder: Optional[Union[int, NaString]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    text_timeOfCreation: Union[XmlPeriod, str, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"\d{4}-\d{4}",
        },
    )
    text_tokenCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_clauseCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text_topicAutom: List[TopicType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    text_note: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner: Optional[TextLearner] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    proficiency: Optional[TextProficiency] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    annotation: Optional[TextAnnotation] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Learner:
    """
    :ivar learner_id: Participant ID assigned by the DAKODA project. A
        related field in CMSCL is `learner_id`.
    :ivar learner_id_orig: Participant ID assigned by the source
        project. A related field in CMSCL is `learner_id`.
    :ivar learner_lCount: Number of languages spoken including L1. There
        is no related field in CMSCL .
    :ivar learner_multipleL1: Does the learner have more than one L1? A
        related field in CMSCL is `learner_L1`.
    :ivar learner_textCount: Number of existing texts from this person.
        There is no related field in CMSCL .
    :ivar learner_note: Any comments regarding this learner/L1 speaker.
        An equivalent field in LC-meta is `learner_note`.
    :ivar sociodemographic:
    :ivar language:
    """

    learner_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_id_orig: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    learner_lCount: Union[int, float, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
            "min_exclusive": 0,
        },
    )
    learner_multipleL1: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_textCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner_note: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    sociodemographic: Optional[Sociodemographics] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    language: List[LanguageOfSpeaker] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class DocumentType:
    class Meta:
        name = "Document_Type"

    corpus: Optional[Corpus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    production_setting: Optional[ProductionSetting] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    task: Optional[TaskBlock] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    learner: Optional[Learner] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text: Optional[TextProperties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    target_hypothesis: List[TargetHypothesis] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    annotator: List[Annotator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class MetaData(DocumentType):
    _json_parser = JsonParser(context=XmlContext(), config=ParserConfig())

    @classmethod
    def from_json_string(cls, json_string):
        return cls._json_parser.parse(io.StringIO(json_string), cls)

    @classmethod
    def from_cas(cls, cas):
        for meta in cas.select(T_META):
            if meta.get("key") == "structured_metadata":
                return cls.from_json_string(meta.get("value"))

        raise ValueError("No structured metadata found in the Document.")

    class Meta:
        name = "document"

    def to_df(self):
        meta_dict = {}
        for key, value in traverse_complex(self):
            meta_dict[key] = value

        return pl.DataFrame(meta_dict)


def traverse_dataclass(
    obj: Any, path: str = ""
) -> Generator[Tuple[str, Any], None, None]:
    """Generator that yields (path, value) tuples for leaf nodes only"""
    if hasattr(obj, "__dataclass_fields__"):
        for field in fields(obj):
            field_value = getattr(obj, field.name)
            current_path = f"{path}.{field.name}" if path else field.name

            print("t:", current_path, " - ", type(field_value))
            if (
                type(field_value) == LanguageOfSpeaker
                or type(field_value) == Annotation
            ):
                # elif isinstance(field_value, (LanguageOfSpeaker, Annotation)):
                # Special handling for LanguageOfSpeaker and Annotation
                ######## TODO
                # for now ignore, see how this can be treated later
                print("----------- HIER -------------")
                pass

            # Only yield if this is a leaf node (not a nested dataclass)
            if hasattr(field_value, "__dataclass_fields__"):
                # This is a nested dataclass, recurse but don't yield
                yield from traverse_dataclass(field_value, current_path)
            else:
                if isinstance(field_value, list):
                    # TODO needs to be handled better
                    # for now only return first element of list
                    if len(field_value) > 0:
                        field_value = field_value[0]
                        if hasattr(field_value, "__dataclass_fields__"):
                            yield from traverse_dataclass(field_value, current_path)
                        elif (
                            type(field_value) == LanguageOfSpeaker
                            or type(field_value) == Annotation
                        ):
                            # elif isinstance(field_value, (LanguageOfSpeaker, Annotation)):
                            # TODO: Special handling for LanguageOfSpeaker and Annotation
                            # for now ignore, see how this can be treated later
                            pass
                    else:
                        field_value = ""

                # This is a leaf node, yield it
                yield (current_path, field_value)


def traverse_complex(
    obj: Any, depth: int = 0
) -> Generator[Tuple[str, Any], None, None]:
    # Prevent infinite recursion with circular references
    obj_id = id(obj)

    if is_dataclass(obj):
        indent = "  " * depth

        for field in fields(obj):
            field_value = getattr(obj, field.name)

            if field_value is None:
                pass
            elif is_dataclass(field_value):
                yield from traverse_complex(field_value, depth + 2)
            elif isinstance(field_value, (list, tuple)):
                for i, item in enumerate(field_value):
                    if is_dataclass(item):
                        yield from traverse_complex(item, depth + 3)
                    else:
                        yield (field.name, item)
            elif isinstance(field_value, dict):
                print(f"dict with {len(field_value)} items")
                for key, value in field_value.items():
                    if is_dataclass(value):
                        yield from traverse_complex(value, depth + 3)
                    else:
                        print(f"{indent}    {key}: {value}")
                        yield (key, value)
            else:
                yield (field.name, field_value)

