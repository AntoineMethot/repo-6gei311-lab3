# swagger_client.CoursApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cours**](CoursApi.md#delete_cours) | **DELETE** /cours/{idcours} | Delete a cours by ID
[**get_cours**](CoursApi.md#get_cours) | **GET** /cours | Retrieve a list of all courses
[**get_cours_by_id**](CoursApi.md#get_cours_by_id) | **GET** /cours/{idcours} | Retrieve a cours by ID
[**get_cours_by_tag**](CoursApi.md#get_cours_by_tag) | **GET** /cours/{tag} | Retrieve a Cours by Tag
[**post_cours**](CoursApi.md#post_cours) | **POST** /cours | Create a new cours


# **delete_cours**
> delete_cours(idcours)

Delete a cours by ID

Delete a cours by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()
idcours = NULL # object | 

try:
    # Delete a cours by ID
    api_instance.delete_cours(idcours)
except ApiException as e:
    print("Exception when calling CoursApi->delete_cours: %s\n" % e)
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

# **get_cours**
> get_cours()

Retrieve a list of all courses

Retrieve a list of all courses

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()

try:
    # Retrieve a list of all courses
    api_instance.get_cours()
except ApiException as e:
    print("Exception when calling CoursApi->get_cours: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cours_by_id**
> get_cours_by_id(idcours)

Retrieve a cours by ID

Retrieve a cours by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()
idcours = NULL # object | ID of cours to return

try:
    # Retrieve a cours by ID
    api_instance.get_cours_by_id(idcours)
except ApiException as e:
    print("Exception when calling CoursApi->get_cours_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idcours** | [**object**](.md)| ID of cours to return | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cours_by_tag**
> get_cours_by_tag(tag)

Retrieve a Cours by Tag

Retrieve a Cours by Tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()
tag = NULL # object | Tags to filter by

try:
    # Retrieve a Cours by Tag
    api_instance.get_cours_by_tag(tag)
except ApiException as e:
    print("Exception when calling CoursApi->get_cours_by_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**object**](.md)| Tags to filter by | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cours**
> post_cours()

Create a new cours

Create a new cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()

try:
    # Create a new cours
    api_instance.post_cours()
except ApiException as e:
    print("Exception when calling CoursApi->post_cours: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

