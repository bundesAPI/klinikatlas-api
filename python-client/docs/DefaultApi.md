# klinikatlas.DefaultApi

All URIs are relative to *https://klinikatlas.api.bund.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fileadmin_json_german_places_json_get**](DefaultApi.md#fileadmin_json_german_places_json_get) | **GET** /fileadmin/json/german-places.json | Liste deutscher Orte abrufen
[**fileadmin_json_german_states_json_get**](DefaultApi.md#fileadmin_json_german_states_json_get) | **GET** /fileadmin/json/german-states.json | Liste deutscher Bundesländer mit Koordinaten abrufen
[**fileadmin_json_icd_codes_json_get**](DefaultApi.md#fileadmin_json_icd_codes_json_get) | **GET** /fileadmin/json/icd_codes.json | Liste der ICD-Codes abrufen
[**fileadmin_json_locations_json_get**](DefaultApi.md#fileadmin_json_locations_json_get) | **GET** /fileadmin/json/locations.json | Liste deutscher Kliniken abrufen
[**fileadmin_json_ops_codes_json_get**](DefaultApi.md#fileadmin_json_ops_codes_json_get) | **GET** /fileadmin/json/ops_codes.json | Liste der OPS-Codes abrufen
[**fileadmin_json_states_json_get**](DefaultApi.md#fileadmin_json_states_json_get) | **GET** /fileadmin/json/states.json | Liste deutscher Bundesländer abrufen
[**krankenhaussuche_krankenhaus_id_get**](DefaultApi.md#krankenhaussuche_krankenhaus_id_get) | **GET** /krankenhaussuche/krankenhaus/{id}/ | Details zu einem spezifischen Krankenhaus abrufen
[**searchresults_get**](DefaultApi.md#searchresults_get) | **GET** /searchresults/ | Suche nach Krankenhäusern basierend auf spezifischen Kriterien


# **fileadmin_json_german_places_json_get**
> [FileadminJsonGermanPlacesJsonGet200ResponseInner] fileadmin_json_german_places_json_get()

Liste deutscher Orte abrufen

### Example


```python
import time
from deutschland import klinikatlas
from deutschland.klinikatlas.api import default_api
from deutschland.klinikatlas.model.fileadmin_json_german_places_json_get200_response_inner import FileadminJsonGermanPlacesJsonGet200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://klinikatlas.api.bund.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = klinikatlas.Configuration(
    host = "https://klinikatlas.api.bund.dev"
)


# Enter a context with an instance of the API client
with klinikatlas.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste deutscher Orte abrufen
        api_response = api_instance.fileadmin_json_german_places_json_get()
        pprint(api_response)
    except klinikatlas.ApiException as e:
        print("Exception when calling DefaultApi->fileadmin_json_german_places_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[FileadminJsonGermanPlacesJsonGet200ResponseInner]**](FileadminJsonGermanPlacesJsonGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreiche Antwort |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fileadmin_json_german_states_json_get**
> [FileadminJsonGermanStatesJsonGet200ResponseInner] fileadmin_json_german_states_json_get()

Liste deutscher Bundesländer mit Koordinaten abrufen

### Example


```python
import time
from deutschland import klinikatlas
from deutschland.klinikatlas.api import default_api
from deutschland.klinikatlas.model.fileadmin_json_german_states_json_get200_response_inner import FileadminJsonGermanStatesJsonGet200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://klinikatlas.api.bund.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = klinikatlas.Configuration(
    host = "https://klinikatlas.api.bund.dev"
)


# Enter a context with an instance of the API client
with klinikatlas.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste deutscher Bundesländer mit Koordinaten abrufen
        api_response = api_instance.fileadmin_json_german_states_json_get()
        pprint(api_response)
    except klinikatlas.ApiException as e:
        print("Exception when calling DefaultApi->fileadmin_json_german_states_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[FileadminJsonGermanStatesJsonGet200ResponseInner]**](FileadminJsonGermanStatesJsonGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreiche Antwort |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fileadmin_json_icd_codes_json_get**
> [FileadminJsonIcdCodesJsonGet200ResponseInner] fileadmin_json_icd_codes_json_get()

Liste der ICD-Codes abrufen

### Example


```python
import time
from deutschland import klinikatlas
from deutschland.klinikatlas.api import default_api
from deutschland.klinikatlas.model.fileadmin_json_icd_codes_json_get200_response_inner import FileadminJsonIcdCodesJsonGet200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://klinikatlas.api.bund.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = klinikatlas.Configuration(
    host = "https://klinikatlas.api.bund.dev"
)


# Enter a context with an instance of the API client
with klinikatlas.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste der ICD-Codes abrufen
        api_response = api_instance.fileadmin_json_icd_codes_json_get()
        pprint(api_response)
    except klinikatlas.ApiException as e:
        print("Exception when calling DefaultApi->fileadmin_json_icd_codes_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[FileadminJsonIcdCodesJsonGet200ResponseInner]**](FileadminJsonIcdCodesJsonGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreiche Antwort |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fileadmin_json_locations_json_get**
> [FileadminJsonLocationsJsonGet200ResponseInner] fileadmin_json_locations_json_get()

Liste deutscher Kliniken abrufen

### Example


```python
import time
from deutschland import klinikatlas
from deutschland.klinikatlas.api import default_api
from deutschland.klinikatlas.model.fileadmin_json_locations_json_get200_response_inner import FileadminJsonLocationsJsonGet200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://klinikatlas.api.bund.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = klinikatlas.Configuration(
    host = "https://klinikatlas.api.bund.dev"
)


# Enter a context with an instance of the API client
with klinikatlas.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste deutscher Kliniken abrufen
        api_response = api_instance.fileadmin_json_locations_json_get()
        pprint(api_response)
    except klinikatlas.ApiException as e:
        print("Exception when calling DefaultApi->fileadmin_json_locations_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[FileadminJsonLocationsJsonGet200ResponseInner]**](FileadminJsonLocationsJsonGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreiche Antwort |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fileadmin_json_ops_codes_json_get**
> [FileadminJsonOpsCodesJsonGet200ResponseInner] fileadmin_json_ops_codes_json_get()

Liste der OPS-Codes abrufen

### Example


```python
import time
from deutschland import klinikatlas
from deutschland.klinikatlas.api import default_api
from deutschland.klinikatlas.model.fileadmin_json_ops_codes_json_get200_response_inner import FileadminJsonOpsCodesJsonGet200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://klinikatlas.api.bund.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = klinikatlas.Configuration(
    host = "https://klinikatlas.api.bund.dev"
)


# Enter a context with an instance of the API client
with klinikatlas.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste der OPS-Codes abrufen
        api_response = api_instance.fileadmin_json_ops_codes_json_get()
        pprint(api_response)
    except klinikatlas.ApiException as e:
        print("Exception when calling DefaultApi->fileadmin_json_ops_codes_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[FileadminJsonOpsCodesJsonGet200ResponseInner]**](FileadminJsonOpsCodesJsonGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreiche Antwort |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fileadmin_json_states_json_get**
> [FileadminJsonStatesJsonGet200ResponseInner] fileadmin_json_states_json_get()

Liste deutscher Bundesländer abrufen

### Example


```python
import time
from deutschland import klinikatlas
from deutschland.klinikatlas.api import default_api
from deutschland.klinikatlas.model.fileadmin_json_states_json_get200_response_inner import FileadminJsonStatesJsonGet200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://klinikatlas.api.bund.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = klinikatlas.Configuration(
    host = "https://klinikatlas.api.bund.dev"
)


# Enter a context with an instance of the API client
with klinikatlas.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste deutscher Bundesländer abrufen
        api_response = api_instance.fileadmin_json_states_json_get()
        pprint(api_response)
    except klinikatlas.ApiException as e:
        print("Exception when calling DefaultApi->fileadmin_json_states_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[FileadminJsonStatesJsonGet200ResponseInner]**](FileadminJsonStatesJsonGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreiche Antwort |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **krankenhaussuche_krankenhaus_id_get**
> str krankenhaussuche_krankenhaus_id_get(id)

Details zu einem spezifischen Krankenhaus abrufen

### Example


```python
import time
from deutschland import klinikatlas
from deutschland.klinikatlas.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://klinikatlas.api.bund.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = klinikatlas.Configuration(
    host = "https://klinikatlas.api.bund.dev"
)


# Enter a context with an instance of the API client
with klinikatlas.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = 1 # int | Eindeutige Kennung des Krankenhauses
    tx_tverzhospitaldata_show_department = "tx_tverzhospitaldata_show[department]_example" # str | Abteilungsfilter (optional)
    tx_tverzhospitaldata_show_geolabel = "tx_tverzhospitaldata_show[geolabel]_example" # str | Geografischer Labelfilter (optional)
    tx_tverzhospitaldata_show_quantile = "tx_tverzhospitaldata_show[quantile]_example" # str | Quantilfilter (optional)
    tx_tverzhospitaldata_show_searchlabel = "tx_tverzhospitaldata_show[searchlabel]_example" # str | Suchlabelfilter (optional)
    c_hash = "cHash_example" # str | Cache-Hash (optional)

    # example passing only required values which don't have defaults set
    try:
        # Details zu einem spezifischen Krankenhaus abrufen
        api_response = api_instance.krankenhaussuche_krankenhaus_id_get(id)
        pprint(api_response)
    except klinikatlas.ApiException as e:
        print("Exception when calling DefaultApi->krankenhaussuche_krankenhaus_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Details zu einem spezifischen Krankenhaus abrufen
        api_response = api_instance.krankenhaussuche_krankenhaus_id_get(id, tx_tverzhospitaldata_show_department=tx_tverzhospitaldata_show_department, tx_tverzhospitaldata_show_geolabel=tx_tverzhospitaldata_show_geolabel, tx_tverzhospitaldata_show_quantile=tx_tverzhospitaldata_show_quantile, tx_tverzhospitaldata_show_searchlabel=tx_tverzhospitaldata_show_searchlabel, c_hash=c_hash)
        pprint(api_response)
    except klinikatlas.ApiException as e:
        print("Exception when calling DefaultApi->krankenhaussuche_krankenhaus_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Eindeutige Kennung des Krankenhauses |
 **tx_tverzhospitaldata_show_department** | **str**| Abteilungsfilter | [optional]
 **tx_tverzhospitaldata_show_geolabel** | **str**| Geografischer Labelfilter | [optional]
 **tx_tverzhospitaldata_show_quantile** | **str**| Quantilfilter | [optional]
 **tx_tverzhospitaldata_show_searchlabel** | **str**| Suchlabelfilter | [optional]
 **c_hash** | **str**| Cache-Hash | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreiche Antwort |  -  |
**404** | Nicht gefunden |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searchresults_get**
> SearchresultsGet200Response searchresults_get()

Suche nach Krankenhäusern basierend auf spezifischen Kriterien

### Example


```python
import time
from deutschland import klinikatlas
from deutschland.klinikatlas.api import default_api
from deutschland.klinikatlas.model.searchresults_get200_response import SearchresultsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://klinikatlas.api.bund.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = klinikatlas.Configuration(
    host = "https://klinikatlas.api.bund.dev"
)


# Enter a context with an instance of the API client
with klinikatlas.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    tx_solr_start = 1 # int | Startindex für die Suchergebnisse (optional)
    tx_solr_rows = 1 # int | Anzahl der zurückzugebenden Zeilen (optional)
    tx_solr_geolabel = "tx_solr[geolabel]_example" # str | Geographisches Label zum Filtern der Ergebnisse (optional)
    tx_solr_latlon = "tx_solr[latlon]_example" # str | Breitengrad und Längengrad zum Filtern der Ergebnisse (optional)
    tx_solr_ops = "tx_solr[ops]_example" # str | OPS-Codes zum Filtern der Ergebnisse (optional)
    tx_solr_searchlabel = "tx_solr[searchlabel]_example" # str | Suchlabel zum Filtern der Ergebnisse (optional)
    tx_solr_icd = "tx_solr[icd]_example" # str | ICD-Codes zum Filtern der Ergebnisse (optional)
    tx_solr_quantile = "tx_solr[quantile]_example" # str | Quantil zum Filtern der Ergebnisse (optional)
    tx_solr_department = "tx_solr[department]_example" # str | Abteilung zum Filtern der Ergebnisse (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Suche nach Krankenhäusern basierend auf spezifischen Kriterien
        api_response = api_instance.searchresults_get(tx_solr_start=tx_solr_start, tx_solr_rows=tx_solr_rows, tx_solr_geolabel=tx_solr_geolabel, tx_solr_latlon=tx_solr_latlon, tx_solr_ops=tx_solr_ops, tx_solr_searchlabel=tx_solr_searchlabel, tx_solr_icd=tx_solr_icd, tx_solr_quantile=tx_solr_quantile, tx_solr_department=tx_solr_department)
        pprint(api_response)
    except klinikatlas.ApiException as e:
        print("Exception when calling DefaultApi->searchresults_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_solr_start** | **int**| Startindex für die Suchergebnisse | [optional]
 **tx_solr_rows** | **int**| Anzahl der zurückzugebenden Zeilen | [optional]
 **tx_solr_geolabel** | **str**| Geographisches Label zum Filtern der Ergebnisse | [optional]
 **tx_solr_latlon** | **str**| Breitengrad und Längengrad zum Filtern der Ergebnisse | [optional]
 **tx_solr_ops** | **str**| OPS-Codes zum Filtern der Ergebnisse | [optional]
 **tx_solr_searchlabel** | **str**| Suchlabel zum Filtern der Ergebnisse | [optional]
 **tx_solr_icd** | **str**| ICD-Codes zum Filtern der Ergebnisse | [optional]
 **tx_solr_quantile** | **str**| Quantil zum Filtern der Ergebnisse | [optional]
 **tx_solr_department** | **str**| Abteilung zum Filtern der Ergebnisse | [optional]

### Return type

[**SearchresultsGet200Response**](SearchresultsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreiche Antwort |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

