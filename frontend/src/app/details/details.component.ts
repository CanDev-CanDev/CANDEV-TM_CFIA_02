import {Component, Input, OnInit} from '@angular/core';
import {Details} from '../models/details';
import {DataService} from '../data.service';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.sass']
})
export class DetailsComponent implements OnInit {

  @Input() company: string;
  details: Details;

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.getDetails(this.company).subscribe(
      details => this.details = details
    );
  }

}
