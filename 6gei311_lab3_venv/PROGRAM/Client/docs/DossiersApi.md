# swagger_client.DossiersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cours_idcours_seances_idseance_dossiers_iddossier_delete**](DossiersApi.md#cours_idcours_seances_idseance_dossiers_iddossier_delete) | **DELETE** /cours/{idcours}/seances/{idseance}/dossiers/{iddossier} | Delete a dossier
[**get_dossier_by_id**](DossiersApi.md#get_dossier_by_id) | **GET** /cours/{idcours}/seances/{idseance}/dossiers/{iddossier} | Get dossier by ID
[**get_dosssiers**](DossiersApi.md#get_dosssiers) | **GET** /cours/{idcours}/seances/{idseance}/dossiers | Get liste de dossiers dans seances
[**post_dossier**](DossiersApi.md#post_dossier) | **POST** /cours/{idcours}/seances/{idseance}/dossiers | Creer dossier dans une seance


# **cours_idcours_seances_idseance_dossiers_iddossier_delete**
> cours_idcours_seances_idseance_dossiers_iddossier_delete(idcours, idseance, iddossier)

Delete a dossier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DossiersApi()
idcours = NULL # object | 
idseance = NULL # object | 
iddossier = NULL # object | 

try:
    # Delete a dossier
    api_instance.cours_idcours_seances_idseance_dossiers_iddossier_delete(idcours, idseance, iddossier)
except ApiException as e:
    print("Exception when calling DossiersApi->cours_idcours_seances_idseance_dossiers_iddossier_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idcours** | [**object**](.md)|  | 
 **idseance** | [**object**](.md)|  | 
 **iddossier** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dossier_by_id**
> get_dossier_by_id(idcours, idseance, iddossier)

Get dossier by ID

Get dossier by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DossiersApi()
idcours = NULL # object | 
idseance = NULL # object | 
iddossier = NULL # object | 

try:
    # Get dossier by ID
    api_instance.get_dossier_by_id(idcours, idseance, iddossier)
except ApiException as e:
    print("Exception when calling DossiersApi->get_dossier_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idcours** | [**object**](.md)|  | 
 **idseance** | [**object**](.md)|  | 
 **iddossier** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dosssiers**
> get_dosssiers(idcours, idseance)

Get liste de dossiers dans seances

Get liste de dossiers dans seances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DossiersApi()
idcours = NULL # object | 
idseance = NULL # object | 

try:
    # Get liste de dossiers dans seances
    api_instance.get_dosssiers(idcours, idseance)
except ApiException as e:
    print("Exception when calling DossiersApi->get_dosssiers: %s\n" % e)
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

# **post_dossier**
> post_dossier(idcours, idseance)

Creer dossier dans une seance

Creer dossier dans une seance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DossiersApi()
idcours = NULL # object | 
idseance = NULL # object | 

try:
    # Creer dossier dans une seance
    api_instance.post_dossier(idcours, idseance)
except ApiException as e:
    print("Exception when calling DossiersApi->post_dossier: %s\n" % e)
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

