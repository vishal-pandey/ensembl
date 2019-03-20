import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router }      from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class MainService {

  constructor(private http: HttpClient,) { }

  // apiUrl = "http://localhost:8000/?path=/";
  apiUrl = "https://ensembl.vishalpandey.xyz/?path=/";

  cFetch(url){
    return this.http.get(url)
  }

}
