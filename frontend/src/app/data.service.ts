import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {News} from './models/news';
import {Details} from './models/details';
import {Recall} from './models/recall';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  readonly root: string = 'http://localhost:5000';

  constructor(private httpClient: HttpClient) { }

  getNews(company: string): Observable<News[]> {
    return this.httpClient.get<News[]>(`${this.root}/news/${company}`);
  }

  getDetails(company: string): Observable<Details> {
    return this.httpClient.get<Details>(`${this.root}/details/${company}`);
  }

  getRecalls(company: string): Observable<Recall[]> {
    return this.httpClient.get<Recall[]>(`${this.root}/recall/${company}`);
  }
}
