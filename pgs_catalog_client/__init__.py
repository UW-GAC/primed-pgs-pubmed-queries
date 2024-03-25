# coding: utf-8

# flake8: noqa

"""
    PGS Catalog REST API

    Programmatic access to the PGS Catalog metadata. More information about the metadata and its structure can be found [here](/docs/).  <i class=\"fas fa-exclamation-circle pgs_color_1\"></i> Each PGS is provided as a scoring file (containing the variants, alleles, effect weights) on our <a href=\"http://ftp.ebi.ac.uk/pub/databases/spot/pgs/scores/\" target=\"_blank\">FTP site</a>. The variants are not distributed within this API; however, a link to the scoring file is provided in the<code>ftp_scoring_file</code>field for each result of the<code>/rest/score/</code>endpoints for ease of download.  ---  ###### REST API settings  * `pagination`: This REST API is using pagination for the endpoints returning more than 1 results. It is currently set to **50** results per page.   <a class=\"toggle_btn pgs_btn_plus\" id=\"pagination\">More information</a>   <div class=\"toggle_content\" id=\"content_pagination\" style=\"display:none\">      ###### **Pagination structure**      Here is an example of the pagination result structure in JSON:      ```       {         \"size\": 50,         \"count\": 137,         \"next\": \"https://www.pgscatalog.org/rest/score/all?limit=50&offset=50\",         \"previous\": null,         \"results\": [           < list the results 1 to 50 >         ]       }     ```     * **size**: is the number of results in the current page.     * **count**: is the overall number of results.     * **next**: is the URL to the following page of results.     * **previous**: is the URL to the preceding page of results (only present if you are not on the first page).     * **results**: contains the list of results of the current page.     <pre></pre>     ###### **Pagination parameters**     * **limit**: The number of results per page can be overwritten using this parameter, e.g:       * <code>.../rest/score/all/?limit=100</code>: returns the first 100 results.       * <code>.../rest/score/all/?limit=150</code>: returns all the results (the overall number of results is 137 in our example above).        The default value is **50**. The maximum value is **250**. Over this maximum value, the REST API returns an error 400.      * **offset**: This parameter indicates the starting position (0 based) of the query in relation to the complete set of results. It provides access to a desired range of results, e.g.:       * <code>.../rest/score/all/?offset=75</code> provides results from the number **76** to **125**, as the number of results per page is **50** by default (equivalent to \"limit=50\")       * <code>.../rest/score/all/?offset=75&limit=60</code> provides results from the number **76** to **135**    </div>   * `rate limit`: The limit number of queries is set to **100** queries per minute.   <a class=\"toggle_btn pgs_btn_plus\" id=\"rate_limit\">More information</a>   <div class=\"toggle_content\" id=\"content_rate_limit\" style=\"display:none\">     Here is an example of the JSON message returned if the rate limit is reached:      ```       {         \"message\": \"request limit exceeded\",         \"availableIn\": \"33 seconds\"       }     ```     * **message**: description of the error.     * **availableIn**: number of seconds before the rate limit is reset.   </div>  ---  <a class=\"toggle_btn pgs_btn_plus\" id=\"changelog\">REST API version changelog</a> <div class=\"toggle_content\" id=\"content_changelog\" style=\"display:none\">    * <span class=\"badge badge-pill badge-pgs\">1.8.6</span> - January 2023:     * New field **date_release** in the Score schemas (`/rest/score/` endpoints), containing the release date of the Score in the PGS Catalog.     * New field **date_release** in the Publication schemas (`/rest/publication/` endpoints), containing the release date of the Publication in the PGS Catalog.    * <span class=\"badge badge-pill badge-pgs\">1.8.5</span> - December 2022:     * Add deprecation message about the parameter 'pgs_ids' of the endpoint `/rest/score/search` as it is redundant with the parameter 'filter_ids'  of the endpoint `/rest/score/all`.     * Fix the parameter 'include_parents' for the endpoint `/rest/trait/all`.     * New parameter 'include_child_associated_pgs_ids' for the endpoint `/rest/trait/all` to display the list of PGS IDs associated with the children traits.    * <span class=\"badge badge-pill badge-pgs\">1.8.4</span> - August 2022:     * New field **ftp_harmonized_scoring_files** in the Score schemas (`/rest/score/` endpoints), listing the URLs to the different harmonized scoring files.     * New field **ensembl_version** in the `/rest/info/` endpoint: Ensembl version used to generate the harmonized scoring files.    * <span class=\"badge badge-pill badge-pgs\">1.8.3</span> - February 2022:     * New parameter 'filter_ids' to narrow down the results in the following endpoints:       * `/rest/score/all`       * `/rest/publication/all`       * `/rest/trait/all`       * `/rest/performance/all`       * `/rest/cohort/all`       * `/rest/sample_set/all`     * New field **name_others** in the Cohort schemas (`/rest/cohort/` endpoints).    * <span class=\"badge badge-pill badge-pgs\">1.8.2</span> - October 2021:     * New field **weight_type** in the Score schemas (`/rest/score/` endpoints).     * New parameters 'pgp_id' and 'pmid' for the endpoints `/rest/performance/search` and `/rest/sample_set/search`.     * New parameter 'pgp_id' for the endpoint `/rest/score/search`.    * <span class=\"badge badge-pill badge-pgs\">1.8.1</span> - July 2021:     * Change the data type of the field **source_PMID** to numeric in the Sample schemas     * New field **source_DOI** in the Sample schemas and move the DOI data from **source_PMID** to this new field.    * <span class=\"badge badge-pill badge-pgs\">1.8</span> - June 2021:     * New endpoint `/rest/api_versions` providing the list of all the REST API versions and their changelogs.     * Change the data type of the field **rest_api/version** in `/rest/info` to **string**.     * Change the data structure of the `/rest/ancestry_categories` endpoint by adding the new fields **display_category** and **categories**.    * <span class=\"badge badge-pill badge-pgs\">1.7</span> - April 2021:     * New data **ancestry_distribution** in the `/rest/score` endpoints, providing information about ancestry distribution on each stage of the PGS.     * New endpoint `/rest/ancestry_categories` providing the list of ancestry symbols and names.     * New data **PMID** (PubMed ID) in the `/rest/info` endpoint, under the **citation** category.    * <span class=\"badge badge-pill badge-pgs\">1.6</span> - March 2021:     * New endpoint `/rest/info` with data such as the REST API version, latest release date and counts, PGS citation, ...     * New endpoint `/rest/cohort/all` returning all the Cohorts and their associated PGS.     * New endpoint `/rest/sample_set/all` returning all the Sample Set data.    * <span class=\"badge badge-pill badge-pgs\">1.5</span> - February 2021:     * Split the array of the field **associated_pgs_ids** (from the `/rest/publication/` endpoint) in 2 arrays **development** and **evaluation**, e.g.:       ```         \"associated_pgs_ids\": {           \"development\": [               \"PGS000011\"           ],           \"evaluation\": [               \"PGS000010\",               \"PGS000011\"           ]         }       ```      * New flag parameter **include_parents** for the endpoint `/rest/trait/all` to display the traits in the catalog + their parent traits (default: 0)    * <span class=\"badge badge-pill badge-pgs\">1.4</span> - January 2021:     * Setup a maximum value for the `limit` parameter.     * Add a new field **size** at the top of the paginated results, to indicate the number of results visible in the page.     * Replace the fields **labels** and **value** under performance_metrics**&rarr;**effect_sizes**/**class_acc**/**othermetrics in the `/rest/performance` endpoints by new fields: **name_long**, **name_short**, **estimate**, **ci_lower**, **ci_upper** and **se**.        Now the content of the **labels** and **value** fields are structured like this, e.g.:       ```         {           \"name_long\": \"Odds Ratio\",           \"name_short\": \"OR\",           \"estimate\": 1.54,           \"ci_lower\": 1.51,           \"ci_upper\": 1.57,           \"se\": 0.0663         }       ```     * Restructure the **samples**&rarr;**sample_age**/**followup_time** JSON (used in several endpoints):       * Merge and replace the fields **mean** and **median** into generic fields **estimate_type** and **estimate**:         ```           \"estimate_type\": \"mean\",           \"estimate\": 53.0         ```       * Merge and replace the fields **se** and **sd** into generic fields **variability_type** and **variability**:         ```           \"variability_type\": \"sd\",           \"variability\": 16.0,         ```       * Merge and replace the fields **range** and **iqr** by a new structure **interval**:         ```           \"interval\": {             \"type\": \"range\",             \"lower\": 51.0,             \"upper\": 77.0           }         ```         Note: The field **type** can take the value 'range', 'iqr' or 'ci'.    * <span class=\"badge badge-pill badge-pgs\">1.3</span> - November 2020:     * New endpoint `/rest/performance/all`.     * New field **license** in the `/rest/score` endpoints.    * <span class=\"badge badge-pill badge-pgs\">1.2</span> - July 2020:     * Update `/rest/trait/search`:       * New parameters '*include_children*' and '*exact*'.       * New field **child_associated_pgs_ids**     * Update `/rest/trait/{trait_id}`:       * New parameter '*include_children*'.       * New field **child_associated_pgs_ids**       * New field **child_traits** present when the parameter '*include_children*' is set to 1.    * <span class=\"badge badge-pill badge-pgs\">1.1</span> - June 2020:     * New endpoint `/rest/trait_category/all`.     * New field **trait_categories** in the `/rest/trait` endpoints.    * <span class=\"badge badge-pill badge-pgs\">1.0</span> - May 2020:     * First version of the PGS Catalog REST API </div>  ---   # noqa: E501

    OpenAPI spec version: 1.8.6
    Contact: pgs-info@ebi.ac.uk
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from pgs_catalog_client.api.other_endpoints_api import OtherEndpointsApi
from pgs_catalog_client.api.performance_metric_endpoints_api import PerformanceMetricEndpointsApi
from pgs_catalog_client.api.publication_endpoints_api import PublicationEndpointsApi
from pgs_catalog_client.api.release_endpoints_api import ReleaseEndpointsApi
from pgs_catalog_client.api.sample_endpoints_api import SampleEndpointsApi
from pgs_catalog_client.api.score_endpoints_api import ScoreEndpointsApi
from pgs_catalog_client.api.trait_endpoints_api import TraitEndpointsApi
# import ApiClient
from pgs_catalog_client.api_client import ApiClient
from pgs_catalog_client.configuration import Configuration
# import models into sdk package
from pgs_catalog_client.models.cohort import Cohort
from pgs_catalog_client.models.cohort_extended import CohortExtended
from pgs_catalog_client.models.cohort_extended_associated_pgs_ids import CohortExtendedAssociatedPgsIds
from pgs_catalog_client.models.demographic import Demographic
from pgs_catalog_client.models.demographic_interval import DemographicInterval
from pgs_catalog_client.models.efo_trait import EFOTrait
from pgs_catalog_client.models.efo_trait_extended import EFOTraitExtended
from pgs_catalog_client.models.efo_trait_ontology import EFOTraitOntology
from pgs_catalog_client.models.efo_trait_ontology_child import EFOTraitOntologyChild
from pgs_catalog_client.models.error4_xx import Error4XX
from pgs_catalog_client.models.inline_response200 import InlineResponse200
from pgs_catalog_client.models.inline_response2001 import InlineResponse2001
from pgs_catalog_client.models.inline_response20010 import InlineResponse20010
from pgs_catalog_client.models.inline_response20010_citation import InlineResponse20010Citation
from pgs_catalog_client.models.inline_response20010_latest_release import InlineResponse20010LatestRelease
from pgs_catalog_client.models.inline_response20010_rest_api import InlineResponse20010RestApi
from pgs_catalog_client.models.inline_response20011 import InlineResponse20011
from pgs_catalog_client.models.inline_response20011_current import InlineResponse20011Current
from pgs_catalog_client.models.inline_response20011_previous import InlineResponse20011Previous
from pgs_catalog_client.models.inline_response2002 import InlineResponse2002
from pgs_catalog_client.models.inline_response2003 import InlineResponse2003
from pgs_catalog_client.models.inline_response2004 import InlineResponse2004
from pgs_catalog_client.models.inline_response2005 import InlineResponse2005
from pgs_catalog_client.models.inline_response2006 import InlineResponse2006
from pgs_catalog_client.models.inline_response2007 import InlineResponse2007
from pgs_catalog_client.models.inline_response2008 import InlineResponse2008
from pgs_catalog_client.models.inline_response2009 import InlineResponse2009
from pgs_catalog_client.models.inline_response_map200 import InlineResponseMap200
from pgs_catalog_client.models.metric import Metric
from pgs_catalog_client.models.pagination import Pagination
from pgs_catalog_client.models.performance_metric import PerformanceMetric
from pgs_catalog_client.models.performance_metric_performance_metrics import PerformanceMetricPerformanceMetrics
from pgs_catalog_client.models.publication import Publication
from pgs_catalog_client.models.publication_extended import PublicationExtended
from pgs_catalog_client.models.release import Release
from pgs_catalog_client.models.sample import Sample
from pgs_catalog_client.models.sample_set import SampleSet
from pgs_catalog_client.models.score import Score
from pgs_catalog_client.models.score_ancestry_distribution import ScoreAncestryDistribution
from pgs_catalog_client.models.score_ancestry_distribution_dev import ScoreAncestryDistributionDev
from pgs_catalog_client.models.score_ancestry_distribution_eval import ScoreAncestryDistributionEval
from pgs_catalog_client.models.score_ancestry_distribution_gwas import ScoreAncestryDistributionGwas
from pgs_catalog_client.models.score_ftp_harmonized_scoring_files import ScoreFtpHarmonizedScoringFiles
from pgs_catalog_client.models.score_ftp_harmonized_scoring_files_grch37 import ScoreFtpHarmonizedScoringFilesGRCh37
from pgs_catalog_client.models.score_ftp_harmonized_scoring_files_grch38 import ScoreFtpHarmonizedScoringFilesGRCh38
from pgs_catalog_client.models.trait_category import TraitCategory
