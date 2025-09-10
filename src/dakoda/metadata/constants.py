from __future__ import annotations

import csv
import json
from decimal import Decimal
from enum import Enum
from pathlib import Path
from typing import Any

from importlib_resources import files
from importlib_resources.abc import Traversable
from xsdata.models.datatype import XmlPeriod

class CustomJSONEncoder(json.JSONEncoder):
    """JSON Encoder that handles all dataclasses."""

    def default(self, obj: Any) -> Any:
        if isinstance(obj, Enum):
            return obj.value
        elif isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, XmlPeriod):
            return str(obj)
        return super().default(obj)


def _enum_from_file(file_path: str | Path | Traversable, separator=","):
    """Creates an enum from a csv file.
    Assumes two columns, first one containing keys, second one values.

    Note:
        Enums created in this way will not have IDE support. This should be fine, as these Enums are only used by the JSONParser in the metadata parsing.
    """

    def decorator(cls):
        enum_dict = {}
        with Path(file_path).open("r") as f:
            reader = csv.reader(f, delimiter=separator)
            for row in reader:
                if not row or len(row) < 2:
                    continue

                key = row[0].strip()
                value = row[1].strip()
                if key:
                    enum_dict[key] = value

        return Enum(cls.__name__, enum_dict)

    return decorator


_type_mappings_dir = files("dakoda.res.type_mappings")


@_enum_from_file(_type_mappings_dir.joinpath("LanguageCode.csv"))
class LanguageCode(Enum):
    """Three letter language codes.

    Attributes are Uppercased, values lowercased.

    Examples:
        >>> LanguageCode.DEU.value == 'deu'
        True
        >>> CountryType.DEU == 'DEU'
        False
        >>> CountryType.DEU == CountryType('deu')
        True
    """

    pass


@_enum_from_file(_type_mappings_dir.joinpath("LanguageGroup.csv"))
class LanguageGroup(Enum):
    pass


@_enum_from_file(_type_mappings_dir.joinpath("LanguageNameDe.csv"))
class LanguageNameDe(Enum):
    pass


@_enum_from_file(_type_mappings_dir.joinpath("LanguageNameEn.csv"))
class LanguageNameEn(Enum):
    pass


@_enum_from_file(_type_mappings_dir.joinpath("CountryType.csv"))
class CountryType(Enum):
    """
    Three-letter country codes defined in ISO 3166-1.
    Attributes are Uppercased.

    Examples:
        >>> CountryType.DEU.value == 'DEU'
        True
        >>> CountryType.DEU == CountryType('DEU')
        True
        >>> CountryType.DEU == 'deu'
        False
    """

    pass


@_enum_from_file(_type_mappings_dir.joinpath("CountryTypeOrNa.csv"))
class CountryTypeOrNa(Enum):
    """
    A country specified as COUNTRY_TYPE or a string indicating that no value is
    available.
    """

    pass


@_enum_from_file(_type_mappings_dir.joinpath("DkdTrgLang.csv"))
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
