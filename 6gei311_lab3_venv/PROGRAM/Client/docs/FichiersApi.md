# swagger_client.FichiersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cours_idcours_seances_idseance_dossiers_iddossier_fichiers_post**](FichiersApi.md#cours_idcours_seances_idseance_dossiers_iddossier_fichiers_post) | **POST** /cours/{idcours}/seances/{idseance}/dossiers/{iddossier}/fichiers | Create a new file for a specific session
[**cours_idcours_seances_idseance_fichiers_get**](FichiersApi.md#cours_idcours_seances_idseance_fichiers_get) | **GET** /cours/{idcours}/seances/{idseance}/fichiers | Retrieve files for a specific session
[**cours_idcours_seances_idseance_fichiers_idfichier_delete**](FichiersApi.md#cours_idcours_seances_idseance_fichiers_idfichier_delete) | **DELETE** /cours/{idcours}/seances/{idseance}/fichiers/{idfichier} | Delete a file by ID
[**cours_idcours_seances_idseance_fichiers_post**](FichiersApi.md#cours_idcours_seances_idseance_fichiers_post) | **POST** /cours/{idcours}/seances/{idseance}/fichiers | Create a new file for a specific session


# **cours_idcours_seances_idseance_dossiers_iddossier_fichiers_post**
> cours_idcours_seances_idseance_dossiers_iddossier_fichiers_post(idcours, idseance, iddossier)

Create a new file for a specific session

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FichiersApi()
idcours = NULL # object | 
idseance = NULL # object | 
iddossier = NULL # object | 

try:
    # Create a new file for a specific session
    api_instance.cours_idcours_seances_idseance_dossiers_iddossier_fichiers_post(idcours, idseance, iddossier)
except ApiException as e:
    print("Exception when calling FichiersApi->cours_idcours_seances_idseance_dossiers_iddossier_fichiers_post: %s\n" % e)
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

# **cours_idcours_seances_idseance_fichiers_get**
> cours_idcours_seances_idseance_fichiers_get(idcours, idseance)

Retrieve files for a specific session

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FichiersApi()
idcours = NULL # object | 
idseance = NULL # object | 

try:
    # Retrieve files for a specific session
    api_instance.cours_idcours_seances_idseance_fichiers_get(idcours, idseance)
except ApiException as e:
    print("Exception when calling FichiersApi->cours_idcours_seances_idseance_fichiers_get: %s\n" % e)
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

# **cours_idcours_seances_idseance_fichiers_idfichier_delete**
> cours_idcours_seances_idseance_fichiers_idfichier_delete(idcours, idseance, idfichier)

Delete a file by ID

Deletea file by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FichiersApi()
idcours = NULL # object | 
idseance = NULL # object | 
idfichier = NULL # object | 

try:
    # Delete a file by ID
    api_instance.cours_idcours_seances_idseance_fichiers_idfichier_delete(idcours, idseance, idfichier)
except ApiException as e:
    print("Exception when calling FichiersApi->cours_idcours_seances_idseance_fichiers_idfichier_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idcours** | [**object**](.md)|  | 
 **idseance** | [**object**](.md)|  | 
 **idfichier** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cours_idcours_seances_idseance_fichiers_post**
> cours_idcours_seances_idseance_fichiers_post(idcours, idseance)

Create a new file for a specific session

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FichiersApi()
idcours = NULL # object | 
idseance = NULL # object | 

try:
    # Create a new file for a specific session
    api_instance.cours_idcours_seances_idseance_fichiers_post(idcours, idseance)
except ApiException as e:
    print("Exception when calling FichiersApi->cours_idcours_seances_idseance_fichiers_post: %s\n" % e)
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

