import {Component, Input, OnInit} from '@angular/core';
import {DataService} from '../data.service';
import {News} from '../models/news';

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.sass']
})
export class NewsComponent implements OnInit {

  @Input() company: string;
  news: News[];

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.getNews(this.company).subscribe(
      news => this.news = news
    );
  }

}
