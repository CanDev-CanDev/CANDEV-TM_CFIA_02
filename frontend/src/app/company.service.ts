import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {

  constructor(private httpClient: HttpClient) { }

  getCompanies(): Observable<string[]> {
    return this.httpClient.get<string[]>('http://localhost:5000/companies');
  }
}
