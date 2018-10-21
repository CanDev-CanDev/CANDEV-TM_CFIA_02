import {Component, Input, OnInit} from '@angular/core';
import {Recall} from '../models/recall';
import {DataService} from '../data.service';

@Component({
  selector: 'app-recall',
  templateUrl: './recall.component.html',
  styleUrls: ['./recall.component.sass']
})
export class RecallComponent implements OnInit {

  @Input() company: string;
  recalls: Recall[];

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.getRecalls(this.company).subscribe(
      recalls => this.recalls = recalls
    );
  }

}
