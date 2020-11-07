/* eslint-disable class-methods-use-this */
import axios from "axios";
import AuthTokenService from "./auth-token.service";

const API_PREFIX_MAP = {
  dev: "http://localhost:8000"
};
class _HttpService {
  // constructor() {
  //   if (process && process.env && process.env.NODE_ENV) {
  //     this.apiGateway =
  //       API_PREFIX_MAP[process.env.NODE_ENV.toLowerCase()] ||
  //       API_PREFIX_MAP.dev;
  //   } else {
  //     this.apiGateway = API_PREFIX_MAP.dev;
  //   }
  // }

  setAPIDomain() {
    this._apiDomain = API_PREFIX_MAP.dev;
  }

  setOrgId(orgId) {
    this.orgId = orgId;
  }

  httpHeaders() {
    return {
      ...AuthTokenService.getAuthHeader()
    };
  }

  prepareUrl = url => {
    return `${this._apiDomain}/${this.orgId}${url}`;
  };

  get(url, params) {
    const reqConfig = {
      method: "get",
      url,
      headers: this.httpHeaders(),
      params
    };
    return this.processRequest(reqConfig);
  }

  post(url, data = {}, params = {}) {
    const reqConfig = {
      method: "post",
      url,
      headers: this.httpHeaders(),
      params,
      data
    };
    return this.processRequest(reqConfig);
  }

  patch(url, data = {}, params = {}) {
    const reqConfig = {
      method: "patch",
      url,
      headers: this.httpHeaders(),
      params,
      data
    };
    return this.processRequest(reqConfig);
  }

  put(url, data = {}, params = {}) {
    const reqConfig = {
      method: "put",
      url,
      headers: this.httpHeaders(),
      params,
      data
    };
    return this.processRequest(reqConfig);
  }

  delete(url, data = {}, params = {}) {
    const reqConfig = {
      method: "delete",
      url,
      headers: this.httpHeaders(),
      params,
      data
    };
    return this.processRequest(reqConfig);
  }

  fileUpload(url, data = {}, params = {}) {
    const headers = this.httpHeaders();
    headers["Content-Type"] = "multipart/form-data";
    const reqConfig = {
      method: "post",
      url,
      headers,
      params,
      data
    };
    return this.processRequest(reqConfig);
  }

  processRequest(reqConfig) {
    const config = {
      ...reqConfig,
      url: this.prepareUrl(reqConfig.url)
    };
    return axios(config)
      .then(response => {
        if (
          response &&
          response.status &&
          response.status >= 200 &&
          response.status < 300
        ) {
          return response.data;
        }
        throw Error(response.statusText);
      })
      .catch(error => {
        // if (
        //   error &&
        //   error.response &&
        //   (error.response.status === 401 || error.response.status === 403)
        // ) {
        //   // handle Un-authorized API requests
        //   this.handleUnauthorized(reqConfig);
        //   return Promise.reject(error.response);
        // }
        if (error && error.response && error.response.status === 401) {
          // handle Un-authorized API requests
          this.handleUnauthorized(reqConfig);
          return Promise.reject(error.response);
        }
        if (error.response && error.response.status >= 500) {
          // handle API server errors in generic way. eg. show "Something went error" in modal
          return Promise.reject(error.response);
        }
        if (error.response && [404, 403, 400].includes(error.response.status)) {
          let errorObj = {};
          if (error && error.response && error.response.data) {
            errorObj = error.response.data;
          } else if (error && error.data) {
            errorObj = error.data;
          }
          return Promise.reject(errorObj);
        }
        if (error.message === "Network Error") {
          return Promise.reject();
        }
        // handling TBD
        let errorObj = {};
        if (error && error.response && error.response.data) {
          errorObj = error.response.data;
        } else if (error && error.data) {
          errorObj = error.data;
        }
        return Promise.reject(errorObj);
      });
  }

  handleUnauthorized(reqConfig) {
    // calling this method to clear authToken from service and local storage
    AuthTokenService.handleLogoutSuccess();
    if (!reqConfig.url.includes("/account/login")) {
      // Re-initializing entire app
      window.location = "/";
    }
  }
}

const HttpService = new _HttpService();
export default HttpService;
