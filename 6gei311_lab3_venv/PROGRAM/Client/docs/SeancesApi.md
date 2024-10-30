# swagger_client.SeancesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_seance**](SeancesApi.md#delete_seance) | **DELETE** /cours/{idcours}/seances/{idseance} | Delete a seance by ID
[**get_seances**](SeancesApi.md#get_seances) | **GET** /cours/{idcours}/seances | Get seances pour a cours
[**get_seances_by_id**](SeancesApi.md#get_seances_by_id) | **GET** /cours/{idcours}/seances/{idseance} | Get a seance by ID
[**get_seances_by_module**](SeancesApi.md#get_seances_by_module) | **GET** /cours/{idcours}/seances/module | Get liste de seance by module
[**get_seances_by_semaine**](SeancesApi.md#get_seances_by_semaine) | **GET** /cours/{idcours}/seances/semaine | Get liste de seance by semaine
[**post_seance**](SeancesApi.md#post_seance) | **POST** /cours/{idcours}/seances | Create a new seance in a cours


# **delete_seance**
> delete_seance(idcours, idseance)

Delete a seance by ID

Delete a seance by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeancesApi()
idcours = NULL # object | 
idseance = NULL # object | 

try:
    # Delete a seance by ID
    api_instance.delete_seance(idcours, idseance)
except ApiException as e:
    print("Exception when calling SeancesApi->delete_seance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idcours** | [**object**](.md)|  | 
 **idseance** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seances**
> get_seances(idcours)

Get seances pour a cours

Get seances pour a cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeancesApi()
idcours = NULL # object | 

try:
    # Get seances pour a cours
    api_instance.get_seances(idcours)
except ApiException as e:
    print("Exception when calling SeancesApi->get_seances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idcours** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seances_by_id**
> get_seances_by_id(idcours, idseance)

Get a seance by ID

Get a seance by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeancesApi()
idcours = NULL # object | 
idseance = NULL # object | 

try:
    # Get a seance by ID
    api_instance.get_seances_by_id(idcours, idseance)
except ApiException as e:
    print("Exception when calling SeancesApi->get_seances_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idcours** | [**object**](.md)|  | 
 **idseance** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seances_by_module**
> get_seances_by_module(idcours, module)

Get liste de seance by module

Get liste de seance by module

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeancesApi()
idcours = NULL # object | 
module = NULL # object | 

try:
    # Get liste de seance by module
    api_instance.get_seances_by_module(idcours, module)
except ApiException as e:
    print("Exception when calling SeancesApi->get_seances_by_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idcours** | [**object**](.md)|  | 
 **module** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seances_by_semaine**
> get_seances_by_semaine(idcours, semaine)

Get liste de seance by semaine

Get liste de seance by semaine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeancesApi()
idcours = NULL # object | 
semaine = NULL # object | 

try:
    # Get liste de seance by semaine
    api_instance.get_seances_by_semaine(idcours, semaine)
except ApiException as e:
    print("Exception when calling SeancesApi->get_seances_by_semaine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idcours** | [**object**](.md)|  | 
 **semaine** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_seance**
> post_seance(idcours)

Create a new seance in a cours

Create a new seance in a cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeancesApi()
idcours = NULL # object | 

try:
    # Create a new seance in a cours
    api_instance.post_seance(idcours)
except ApiException as e:
    print("Exception when calling SeancesApi->post_seance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idcours** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

